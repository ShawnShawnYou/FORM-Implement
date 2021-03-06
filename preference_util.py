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
    if is_case_1(preferences):
        return False
    ret = True
    for i in preferences:
        if len(i) != 1:
            ret = False
            break
    return ret


def is_case_3(preferences):
    if is_case_1(preferences):
        return False
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


def verify_match(match, skip_bug):
    # 验证匹配无误（不验证block pair，只验证是不是有bug）
    verification_result = {
        'single_dog': 0,
        'has_partner': 0,
        'wrong_match': 0,
        'long_list': 0,
    }

    for i in range(len(match)):
        if len(match[i]) == 1:
            if match[i][0] == i:
                verification_result['single_dog'] = verification_result['single_dog'] + 1
            else:
                partner = match[i][0]
                if match[partner][0] == i:
                    verification_result['has_partner'] = verification_result['has_partner'] + 1
                else:
                    verification_result['wrong_match'] = verification_result['wrong_match'] + 1
                    if skip_bug:
                        match[i] = [i]

        else:
            verification_result['long_list'] = verification_result['long_list'] + 1
            if skip_bug:
                match[i] = [i]

    return match, verification_result


def fairness_compute(original_preference, match, start_with=1):

    if start_with == 1:
        transfer_preferences_start_with_1(original_preference)

    unfair_count = 0
    none_count = 0

    for i in range(len(match)):
        if match[i] is None:
            none_count += 1
            continue

        partner = match[i][0]

        if i == partner:
            continue

        index_partner = find_target_in_row(original_preference, i, partner)
        if index_partner is None:
            continue

        # 考察i的list里面比当前的partner好的那些
        for j in range(0, index_partner):
            # 第一个倒霉蛋
            to_be_block_i = original_preference[i][j]

            # 第一个倒霉蛋现在的配偶
            if match[to_be_block_i] is None:
                continue
            to_be_block_i_partner = match[to_be_block_i][0]

            # 第一个倒霉蛋现在的配偶的位置（如果是他自己就排在最后）
            to_be_block_i_partner_index = find_target_in_row(original_preference, to_be_block_i, to_be_block_i_partner)
            if to_be_block_i_partner_index is None:
                to_be_block_i_partner_index = len(original_preference[to_be_block_i_partner])

            # 当前i在第一个倒霉蛋心目的位置
            i_index = find_target_in_row(original_preference, to_be_block_i, i)

            if i_index < to_be_block_i_partner_index:
                # 他俩可以私奔
                unfair_count += 1
                break

    return unfair_count, none_count
