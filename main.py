
import test_dataset_array
from BSRM import basic_stable_roommate_matching
import random
from preference_util import *
from datetime import datetime


def random_complete_test_data(data_size=200, start_with=1):

    test_data = []

    min_index = start_with
    max_index = data_size + start_with - 1

    for i in range(min_index, max_index + 1):
        tmp = []
        for j in range(min_index, max_index + 1):
            if i != j:
                tmp.append(j)

        random.shuffle(tmp)
        test_data.append(tmp)

    return test_data


def random_incomplete_test_data(data_size=200, start_with=1):

    complete_data = random_complete_test_data(data_size)

    delete_pair_num = random.randint(1, int((data_size * (data_size - 1)) / 2))

    for i in range(delete_pair_num):

        index_delete_i = random.randint(0, data_size - 1)

        while len(complete_data[index_delete_i]) == 0:
            index_delete_i = (index_delete_i + 1) % data_size

        # 在j的list里面有的叫actual
        actual_delete_i = index_delete_i + start_with

        index_delete_j = len(complete_data[index_delete_i])

        del complete_data[index_delete_i][index_delete_j]

        index_delete_i = find_target_in_row(complete_data, index_delete_j, actual_delete_i)

        del complete_data[index_delete_j][index_delete_i]


def batch_test(count=200, data_size=200, start_with=1, debug=True):

    count_list = [0 for i in range(5)]

    for round in range(count):

        test_data = random_complete_test_data(data_size, start_with)

        print(round)
        if debug:
            print("preferences", test_data)

        type, msg, result = basic_stable_roommate_matching(test_data, start_with)
        count_list[type] = count_list[type] + 1

        if debug:
            print(msg, result)
            print()

        # if msg == "bug":
        #     break

    summary = {'bug': count_list[0],
               'after phase_1 find answer': count_list[1],
               'unsolvable by phase_1': count_list[2],
               'after phase_2 find answer': count_list[3],
               'unsolvable by phase_2': count_list[4]}
    print(summary)


if __name__ == '__main__':

    # TODO: incomplete list
    batch_test(count=200, data_size=10, start_with=1, debug=True)
    # batch_test(1, 5)

    # test_data = test_dataset_array.test_match_6
    #
    # type, msg, result = basic_stable_roommate_matching(test_data)
    #
    # print(type, msg, result)