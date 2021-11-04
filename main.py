
import test_dataset_array
from BFRM import basic_stable_roommate_matching
import random
from preference_util import *
from datetime import datetime
import time
from tqdm import tqdm


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

    test_data = random_complete_test_data(data_size)

    delete_pair_num = random.randint(1, int((data_size * (data_size - 1)) / 2))

    for i in range(delete_pair_num):

        index_delete_i = random.randint(0, data_size - 1)

        while len(test_data[index_delete_i]) == 0:
            index_delete_i = (index_delete_i + 1) % data_size

        # 在j的list里面有的叫actual
        actual_delete_i = index_delete_i + start_with

        index_delete_j = test_data[index_delete_i][len(test_data[index_delete_i]) - 1] - start_with

        del test_data[index_delete_i][len(test_data[index_delete_i]) - 1]

        index_delete_i = find_target_in_row(test_data, index_delete_j, actual_delete_i)

        del test_data[index_delete_j][index_delete_i]

    return test_data


def batch_test(count=200, data_size=200, start_with=1, debug=True):

    count_list = [0 for i in range(5)]
    empty = 0

    for round in tqdm(range(count)):

        test_data = random_incomplete_test_data(data_size, start_with)

        if debug:
            print("preferences", test_data)

        type, msg, result = basic_stable_roommate_matching(test_data, start_with)
        for i in result:
            if len(i) == 0:
                empty = empty + 1

        count_list[type] = count_list[type] + 1

        if debug:
            print(msg, result)
            print()

        # if msg == "bug":
        #     break

    summary = {'avg empty': empty / 200.0,
               'bug': count_list[0],
               'after phase_1 find answer': count_list[1],
               'unsolvable by phase_1': count_list[2],
               'after phase_2 find answer': count_list[3],
               'unsolvable by phase_2': count_list[4]}
    print(summary)


if __name__ == '__main__':

    start = time.time()
    batch_test(count=800, data_size=200, start_with=1, debug=False)
    end = time.time()
    print("运行时间:%.2f秒" % (end - start))
    # output:循环运行时间:5.50秒


    # test_data = test_dataset_array.test_match_7
    #
    # type, msg, result = basic_stable_roommate_matching(test_data)
    #
    # print(type, msg, result)