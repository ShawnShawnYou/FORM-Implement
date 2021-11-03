from preference_util import *


def phase_1_old(preferences):
    # 问题：删除清洗应该是在同一步，如果删除的是某个的第一位，那么那一个应该重新删一次，同时要使用freelist
    first_list = [None for i in range(len(preferences))]
    for i in range(len(preferences)):
        index = 0
        first_row = preferences[preferences[i][0]]
        for j in range(len(first_row)):
            if first_row[j] == i:
                index = j
                break

        if first_list[preferences[i][0]] is None or first_list[preferences[i][0]] > index:
            first_list[preferences[i][0]] = index

    # reduce
    p1_reduced_preferences = preferences
    free_list = [False for i in range(len(preferences))]
    for i in range(len(preferences)):
        if first_list[i] is not None:
            to_be_delete = preferences[i][(first_list[i] + 1): ]
            p1_reduced_preferences = delete_pair(p1_reduced_preferences, i, preferences[i][first_list[i]], False)
            # 这里有问题
        # else:
        #     p1_reduced_preferences[i] = preferences[i]

    # reduce清洗（把一些未配对的match删除）
    p1_reduced_preferences = refresh_preferences_alone_pair(p1_reduced_preferences)

    return p1_reduced_preferences


def phase_1_old2(preferences):
    # 问题：这一版只遍历了一遍整个矩阵，没有考虑first会更新的情况
    for i in range(len(preferences)):

        first = preferences[i][0]

        if first is not None:
            preferences = delete_pair(preferences, first, i, False)

    return preferences


def phase_1(preferences):

    check_set = set(i for i in range(len(preferences)))

    while len(check_set) > 0 and not is_case_1(preferences):

        now_check = check_set.pop()

        first = preferences[now_check][0]

        if first is not None:
            index_of_now_check = find_target_in_row(preferences, first, now_check)

            if index_of_now_check is None:
                to_be_delete = []
            else:
                to_be_delete = preferences[first][index_of_now_check + 1:]
            for i in to_be_delete:
                preferences = delete_pair(preferences, check_set, first, i)

    return preferences
