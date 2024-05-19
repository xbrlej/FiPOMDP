from typing import Tuple, Dict

from fimdp.core import ActionData


class OnlineStrategy:
    def update_obs(self, outcome: int) -> None:
        """Method signalizing the tree the new observation outcome

        Parameters
        ----------
        outcome : int
            Given observation outcome
        """
        pass

    def next_action(self, iterations_count: int = 1000) -> ActionData:
        """Method for getting the next action.

        Parameters
        ----------
        iterations_count : int
            Max iterations for the POMCP simulation

        Returns
        -------
        ActionData
            Action picked by POMCP simulation.
        """
        pass

    def reset(
            self,
            init_energy: int,
            init_obs: int,
            init_bel_supp: Tuple[int, ...],
            exploration: float,
            init_belief: Dict[int, float],
            random_seed: int = 42,
    ) -> None:
        """Method for resetting the strategy with new initial conditions.

        Parameters
        ----------
        init_energy : int
            New initial energy.
        init_obs : int
            New initial observation.
        init_bel_supp : int
            New initial belief support.
        init_belief : Dict[int, float]
            New initial belief/particle filter result.
        exploration : float
            New exploration constant
        random_seed : int
            Random seed, defaults to 42.
        """
        pass
