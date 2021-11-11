import random
from copy import deepcopy

import phase_1
from preference_util import *
from algorithm_config import *


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
                if len(preferences[j]) > 0:
                    first_preference = preferences[j][0]
                    if second_preference == first_preference:
                        ht_graph[i].append(j)

    return ht_graph


def choose_max_regret(preferences, original_preferences, last_candidate):
    delta = 1
    continue_flag = True
    while continue_flag:
        continue_flag = False
        for i in range(len(original_preferences)):
            old_len = len(original_preferences[i])
            if old_len >= delta:
                continue_flag = True
                last_one = original_preferences[i][old_len - delta]
                if last_one in preferences[i] and last_one in last_candidate:
                    return last_one
        delta = delta + 1

    last_one = last_candidate.pop()
    last_candidate.add(last_one)
    return last_one


def choose_min_value(preferences, original_preferences, original_individual_cost_saving,
                     last_candidate):
    min_value_index = 0
    min_value_partner = 0
    min_value = 9999

    tmp_last_candidate = deepcopy(last_candidate)
    for i in range(len(tmp_last_candidate)):
        last_partner = tmp_last_candidate.pop()
        last_one = preferences[last_partner][-1]
        if last_partner == last_one:
            continue

        i_in_last_one_index = find_target_in_row(original_preferences, last_one, last_partner)
        value_last_one = original_individual_cost_saving[last_one][i_in_last_one_index]

        if value_last_one < min_value:
            min_value = value_last_one
            min_value_index = last_one
            min_value_partner = last_partner

    return min_value_index, min_value_partner


def is_big_cycle(preferences, rotation):
    list_all_set = set()
    list_2_set = set()
    for i in rotation:
        list_i = preferences[i]
        for j in range(len(list_i)):
            if j <= 1:
                list_2_set.add(list_i[j])
            list_all_set.add(list_i[j])

    if len(list_all_set - list_2_set) == 0:
        return True
    else:
        return False


def filter_rotation_list(preferences, rotation_list):
    rotation_candidate = []
    for rotation in rotation_list:
        if len(rotation) % 2 == 0 or not is_big_cycle(preferences, rotation):
            rotation_candidate.append(rotation)
    return rotation_candidate


def find_rotation_list(preferences, original_preferences, original_individual_cost_saving):
    # 用集合去除重复路径
    rotation_set = set()

    ht_graph = get_ht_graph(preferences)

    if config['strategy'] == 2:
        tmp_list = []
        for i in range(len(ht_graph)):
            if ht_graph[i] != []:
                tmp_list.append(i)

        last_candidate = set(tmp_list)

        while len(rotation_set) == 0 and len(last_candidate) > 0:
            # last_one = choose_max_regret(preferences, original_preferences, last_candidate)
            last_one, last_one_partner = choose_min_value(preferences, original_preferences, original_individual_cost_saving,
                                        last_candidate)
            to_visit = set([i for i in range(len(ht_graph))])
            dfs(rotation_set, ht_graph, [], last_one, to_visit)
            last_candidate.remove(last_one_partner)
    else:
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


def get_rotation_value(rotation, preferences,
                       original_preferences, original_individual_cost_saving):
    y_set = [preferences[i][0] for i in rotation]

    value = 0
    for i in range(len(rotation)):
        x_i = rotation[i]

        y_i_plus_1 = y_set[(i + 1) % len(y_set)]
        position_1 = find_target_in_row(original_preferences, x_i, y_i_plus_1)
        u_1 = -1 * original_individual_cost_saving[x_i][position_1]

        y_i = y_set[i]
        position_2 = find_target_in_row(original_preferences, x_i, y_i)
        u_2 = -1 * original_individual_cost_saving[x_i][position_2]

        value = value + (u_1 - u_2)

    return value


def choose_rotation(rotation_list, preferences,
                    original_preferences, original_individual_cost_saving):
    if config['strategy'] == 3:
        min_index = 0
        for i in range(1, len(rotation_list)):
            value_min = get_rotation_value(rotation_list[min_index], preferences,
                                           original_preferences, original_individual_cost_saving)

            value_i = get_rotation_value(rotation_list[i], preferences,
                                         original_preferences, original_individual_cost_saving)

            if value_min > value_i:
                min_index = i
        return min_index
    else:
        return random.randint(0, len(rotation_list) - 1)


def phase_2(preferences, original_preferences, original_individual_cost_saving):
    bug_flag = False
    while is_case_3(preferences):
        rotation_list = find_rotation_list(preferences,
                                           original_preferences, original_individual_cost_saving)
        # rotation_list = filter_rotation_list(preferences, rotation_list)

        if len(rotation_list) > 0:
            bug_flag = False
            chosen_rotation_index = choose_rotation(rotation_list, preferences,
                                                    original_preferences, original_individual_cost_saving)
            rotation = rotation_list[chosen_rotation_index]

            preferences = eliminate_rotation(preferences, rotation)

            preferences = phase_1.phase_1(preferences)
        else:
            if not bug_flag:
                # 防止[[3], [2, 7], [4, 1], [0], [2], [9], [], [1], [], [5]] 这种情况
                preferences = phase_1.phase_1(preferences)
                bug_flag = True
                continue
            else:
                return 4, "unsolvable by phase_2", preferences
    if is_case_2(preferences):
        return 3, "after phase_2 find answer", preferences
    # elif is_case_4(preferences):
    #     return 3, "after phase_2 find answer with single dog", preferences
    else:
        return 4, "unsolvable by phase_2", preferences

