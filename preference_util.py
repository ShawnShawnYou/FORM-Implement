"""
• Case1: has empty.
• Case2: all one.
• Case3: Some more than one. not (<= 1)

• my case 4: all <= 1 and not have duplicated like {[0], [1], [0]}
"""


def is_case_1(preferences):
    ret = False
    for i in preferences:
        if len(i) == 0:
            ret = True
            break
    return ret


def is_case_2(preferences):
    ret = True
    for i in preferences:
        if len(i) != 1:
            ret = False
            break
    return ret


def is_case_3(preferences):
    ret = False
    for i in preferences:
        if len(i) > 1:
            ret = True
            break
    return ret


def is_case_4(preferences):
    duplicated_set = set()
    ret = True
    for i in preferences:
        if len(i) > 1:
            ret = False
            break
        if len(i) == 1:
            if i[0] in duplicated_set:
                ret = False
                break
            else:
                duplicated_set.add(i[0])
    return ret


def find_target_in_row(preferences, row, target):
    for index in range(len(preferences[row])):
        if preferences[row][index] == target:
            return index
    return None


def delete_pair(preferences, check_set, p1: int, p2: int):

    index_p2 = find_target_in_row(preferences, p1, p2)
    index_p1 = find_target_in_row(preferences, p2, p1)

    if index_p2 == 0:
        check_set.add(p1)
    if index_p1 == 0:
        check_set.add(p2)

    del preferences[p1][index_p2]
    del preferences[p2][index_p1]

    return preferences


def refresh_preferences_alone_pair(preferences):
    for i in range(len(preferences)):
        flag = True
        while flag:
            flag = False
            check_row = preferences[i]
            for j in range(len(check_row)):
                if i not in preferences[check_row[j]]:
                    del preferences[i][j]
                    flag = True
                    break
    return preferences


def add_dummy_node(preferences, start_with=1):
    dummy_i = len(preferences) + start_with


def eliminate_single(preferences):
    for i in range(len(preferences)):
        if len(preferences[i]) == 0:
            preferences[i] = [i]
    return preferences


def transfer_preferences_start_with_1(preferences):
    for i in preferences:
        for j in range(len(i)):
            i[j] = i[j] - 1

    return preferences
