from typing import Tuple

from fimdp.core import ActionData
from fipomdp import ConsPOMDP
from fipomdp.pomcp_utils import matching_state_action, sample_from_distr


def simulate_observation(cpomdp: ConsPOMDP, bs_action: ActionData, src_state: int) -> Tuple[int, int]:
    cpomdp_action = matching_state_action(cpomdp, bs_action, src_state)
    new_state = sample_from_distr(cpomdp_action.distr)
    new_obs = sample_from_distr(cpomdp.get_state_obs_probs(new_state))
    return new_state, new_obs
