
import phase_1
import phase_2
from preference_util import *

from copy import deepcopy


def transfer_preferences_start_with_1(preferences):
    for i in preferences:
        for j in range(len(i)):
            i[j] = i[j] - 1

    return preferences


def basic_stable_roommate_matching(preferences_array, start_with=1):

    if start_with == 1:
        preferences_array = transfer_preferences_start_with_1(preferences_array)

    # original_preferences 用于debug看看原始矩阵
    original_preferences = deepcopy(preferences_array)

    phase_1_reduced_preferences = phase_1.phase_1(preferences_array)
    #
    # phase_1_reduced_preferences = eliminate_single(phase_1_reduced_preferences)

    # 直接跳过phase_1是不行的 因为有末尾的约束 所以phase2的一定找得到rotation的定理才有效
    if is_case_2(phase_1_reduced_preferences):
        return 1, "after phase_1 find answer", phase_1_reduced_preferences

    # if is_case_4(phase_1_reduced_preferences):
    #     return 1, "after phase_1 find answer", phase_1_reduced_preferences

    # if is_case_1(phase_1_reduced_preferences):
    #     return 2, "unsolvable by phase_1", phase_1_reduced_preferences

    phase_2_reduced_preferences = phase_2.phase_2(phase_1_reduced_preferences)

    return phase_2_reduced_preferences
