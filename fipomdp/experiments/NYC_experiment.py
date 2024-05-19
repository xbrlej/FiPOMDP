#!/usr/bin/env python3
import logging

from fipomdp.config.config_utils import ConfigUtils
from fipomdp.experiments.utils import syspath

syspath.init()
import platform
import time
from statistics import stdev
from typing import List, Tuple

import psutil
from joblib import Parallel, delayed

from fimdp.objectives import BUCHI
from fipomdp import ConsPOMDP
from fipomdp.energy_solvers import ConsPOMDPBasicES
from fipomdp.environments.NYC_environment import NYCPOMDPEnvironment
from fipomdp.experiments.utils.observation_util import simulate_observation
from fipomdp.pomcp import POMCPStrategy

from fipomdp.reward_functions import consumption_based
from fipomdp.experiments.utils.threads_macro import THREADS


def nyc_experiment(computed_cpomdp: ConsPOMDP,
                   computed_solver: ConsPOMDPBasicES,
                   capacity: int, targets: List[int],
                   random_seed: int,
                   config_section: str,
                   logger,
                   ) ->  Tuple[int, bool, List[int], List[int], bool, int]:
    if computed_cpomdp.belief_supp_cmdp is None or computed_solver.bs_min_levels[BUCHI] is None:
        raise AttributeError(f"Given CPOMDP or its solver is not pre computed!")

    rollout_function = consumption_based

    #   HYPER PARAMETERS NEEDED FOR EXPERIMENTS

    parameters = ConfigUtils().get_config_property(config_section)
    actual_horizon = parameters['horizon']
    init_bel_supp = eval(parameters['init_belief_support'])
    max_iterations = parameters["iterations"]

    strategy = POMCPStrategy(
        config_section,
        computed_cpomdp,
        capacity,
        targets,
        rollout_function,
        random_seed,
        recompute=False,
        solver=computed_solver,
        logger=logger,
    )

    simulated_state = init_bel_supp[0]

    path = [simulated_state]

    logger.info(f"\nLAUNCHING with max iterations: {max_iterations}\n")
    reward = 0
    target_hit = False
    decision_times = []

    for _ in range(actual_horizon):
        pre_decision_time = time.time()
        action = strategy.next_action(max_iterations)
        simulated_state, new_obs = simulate_observation(computed_cpomdp, action, simulated_state)
        path.append(simulated_state)
        reward -= action.cons
        if simulated_state in targets:
            reward += 1000
            target_hit = True
            break

        strategy.update_obs(new_obs)
        decision_times.append(round(time.time() - pre_decision_time))

    logger.info(f"\n--------EXPERIMENT FINISHED---------")
    logger.info(f"--------RESULTS--------")

    logger.info(f"For max iterations: {max_iterations}, target has been reached {target_hit} times.")
    logger.info(f"Path of the agent was: {path}")
    logger.info(f"Decision times: {decision_times}")
    logger.info(f"Decision time average: {sum(decision_times)/len(decision_times)}, standard deviation: {stdev(decision_times)}")
    logger.info(f"Target hit: {target_hit}, reward: {reward}")

    return max_iterations, target_hit, path, decision_times, target_hit, reward


def log_experiment_with_seed(cpomdp, env, i, log_file_name, solver, targets):

    config_section = "HYPERPARAMETERS_NYC"

    handler = logging.FileHandler(f"./logs/logs_NYC/{log_file_name}{i}.log", 'w')
    formatter = logging.Formatter("%(asctime)s %(levelname)-8s %(message)s")
    handler.setFormatter(formatter)
    logger = logging.getLogger(f"{i}")
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    logger.addHandler(handler)
    logger.level = logging.INFO
    logger.info("START")
    uname = platform.uname()
    logger.info(f"Node name: {uname.node}")
    logger.info(f"System: {uname.system}")
    logger.info(f"Release: {uname.release}")
    logger.info(f"Version: {uname.version}")
    logger.info(f"Machine: {uname.machine}")
    logger.info(f"Processor: {uname.processor}")
    logger.info(f"RAM: {str(round(psutil.virtual_memory().total / (1024.0 ** 3)))} GB")
    return nyc_experiment(cpomdp, solver, env.cmdp_env.capacity, targets, i, config_section, logger)


def main():
    log_file_name = "NYCExperiments"  # Change for your needs
    logging_level = logging.INFO
    # set to INFO (20) for logging to be active, set to DEBUG (10) for details,
    # set to 5 for extreme debug

    logging.basicConfig(
        filename=f"logs/{log_file_name}.log",
        filemode="w",  # Erase previous log
        format="%(asctime)s %(levelname)-8s %(message)s",
        level=logging_level,
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    capacity = ConfigUtils().get_config_property("HYPERPARAMETERS_NYC")['capacity']

    env = NYCPOMDPEnvironment(capacity)
    cpomdp, targets = env.get_cpomdp()

    preprocessing_start = time.time()

    cpomdp.compute_guessing_cmdp_initial_state([cpomdp.state_with_name('42459137')])

    solver = ConsPOMDPBasicES(cpomdp, [cpomdp.state_with_name('42459137')], env.cmdp_env.capacity, targets)
    solver.compute_buchi()

    init_obs = cpomdp.state_with_name('42459137')
    init_bel_supp = tuple([cpomdp.state_with_name('42459137')])

    props = ConfigUtils().get_config_property("HYPERPARAMETERS_NYC")
    props['init_belief_support'] = init_bel_supp
    props['init_observation'] = init_obs
    ConfigUtils().set_config_property("HYPERPARAMETERS_NYC", props)

    preprocessing_time = round(time.time() - preprocessing_start)

    results = Parallel(n_jobs=THREADS)(
        delayed(log_experiment_with_seed)(cpomdp, env, i, log_file_name, solver, targets) for i in range(100))

    logging.info(f"RESULTS (): {results}")
    print(preprocessing_time)

if __name__ == "__main__":
    main()

