from preference_util import *


def greedy_roommate_matching(preferences_array, start_with=1):

    if start_with == 1:
        preferences_array = transfer_preferences_start_with_1(preferences_array)
