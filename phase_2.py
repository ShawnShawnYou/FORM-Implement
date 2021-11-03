from copy import deepcopy

import phase_1
from preference_util import *


def eliminate_rotation(preferences, rotation):
    y_set = [preferences[i][0] for i in rotation]

    for i in range(len(y_set)):
        y_i = y_set[i]

        x_i_minus_1 = rotation[0 if y_i == len(y_set) else i - 1]

        index = find_target_in_row(preferences, y_i, x_i_minus_1)

        if index is None:
            continue
        to_be_delete = preferences[y_i][index + 1:]
        # TODO: 可能有问题 TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'

        for j in to_be_delete:
            preferences = delete_pair(preferences, set([]), y_i, j)

    preferences = refresh_preferences_alone_pair(preferences)

    return preferences


def dfs(ans, graph, trace, start, to_visit):

    if not start in to_visit:
        return

    if len(graph[start]) == 0:
        to_visit.remove(start)
        return

    # 深拷贝，对不同起点，走过的路径不同
    trace = deepcopy(trace)

    # 如果下一个点在trace中，则返回环
    if start in trace:
        index = trace.index(start)
        tmp = [str(i) for i in trace[index:]]
        ans.add(str(' '.join(tmp)))

        return

    trace.append(start)

    for i in graph[start]:
        dfs(ans, graph, trace, i, to_visit)

    if start in to_visit:
        to_visit.remove(start)


def get_ht_graph(preferences):
    ht_graph = [[] for i in preferences]
    for i in range(len(preferences)):
        if len(preferences[i]) >= 2:
            second_preference = preferences[i][1]

            for j in range(len(preferences)):
                if i == j:
                    continue
                first_preference = preferences[j][0]
                if second_preference == first_preference:
                    ht_graph[i].append(j)

    return ht_graph


def find_rotation_list(preferences):
    # 用集合去除重复路径
    rotation_set = set()

    ht_graph = get_ht_graph(preferences)

    # 考虑如果是图中有多个连通分支
    to_visit = set([i for i in range(len(ht_graph))])
    while len(to_visit) != 0:
        start = to_visit.pop()
        to_visit.add(start)
        dfs(rotation_set, ht_graph, [], start, to_visit)

    # rotation_set = {'2 4', '0 1 3', '0 1 2 3', '0 1 2'}字符串集合转为二维rotation_list
    rotation_list = []
    for i in rotation_set:
        rotation = i.split(" ")
        rotation = [int(j) for j in rotation]
        rotation_list.append(rotation)

    return rotation_list


def get_rotation_value(rotation):
    ret = len(rotation)
    return ret


def choose_rotation(rotation_list):
    max_index = 0
    for i in range(1, len(rotation_list)):
        if get_rotation_value(rotation_list[max_index]) < \
                get_rotation_value(rotation_list[i]):
            max_index = i
    return max_index


def phase_2(preferences):
    while is_case_3(preferences):
        rotation_list = find_rotation_list(preferences)

        if len(rotation_list) > 0:
            chosen_rotation_index = choose_rotation(rotation_list)
            rotation = rotation_list[chosen_rotation_index]

            preferences = eliminate_rotation(preferences, rotation)

            preferences = phase_1.phase_1(preferences)
        else:
            return 0, "bug", preferences
    if is_case_2(preferences):
        return 3, "after phase_2 find answer", preferences
    elif is_case_4(preferences):
        return 3, "after phase_2 find answer with single dog", preferences
    else:
        return 4, "unsolvable by phase_2", preferences

