from preference_util import *


def greedy_roommate_matching(preferences, overall_sorted_list, start_with=1):

    if start_with == 1:
        preferences = transfer_preferences_start_with_1(preferences)

    check_set = set([i for i in range(len(preferences))])

    for to_be_delete in range(overall_sorted_list):

        p1 = to_be_delete.id - start_with
        p2 = to_be_delete.match_id - start_with

        if p1 in check_set and p2 in check_set:
            preferences[p1] = [p2]
            preferences[p2] = [p1]
            check_set.remove(p1)
            check_set.remove(p2)

    return preferences
