
import phase_1
import phase_2
from preference_util import *

from copy import deepcopy
from algorithm_config import *


def basic_stable_roommate_matching(preferences_array, original_individual_cost_saving, start_with=1):

    if start_with == 1:
        preferences_array = transfer_preferences_start_with_1(preferences_array)

    # original_preferences 用于debug看看原始矩阵
    original_preferences = deepcopy(preferences_array)

    phase_1_reduced_preferences = phase_1.phase_1(preferences_array)

    if len(phase_1_reduced_preferences) % 2 == 1 and not is_case_1(phase_1_reduced_preferences):
        return 2, "unsolvable by phase_1", phase_1_reduced_preferences

    phase_1_reduced_preferences = eliminate_single(phase_1_reduced_preferences)

    # 直接跳过phase_1是不行的 因为有末尾的约束 所以phase2的一定找得到rotation的定理才有效
    if is_case_2(phase_1_reduced_preferences):
        return 1, "after phase_1 find answer", phase_1_reduced_preferences

    # if is_case_4(phase_1_reduced_preferences):
    #     return 1, "after phase_1 find answer", phase_1_reduced_preferences

    # if is_case_1(phase_1_reduced_preferences):
    #     return 2, "unsolvable by phase_1", phase_1_reduced_preferences

    phase_2_reduced_preferences = phase_2.phase_2(phase_1_reduced_preferences,
                                                  original_preferences, original_individual_cost_saving)

    return phase_2_reduced_preferences
