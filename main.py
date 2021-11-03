
import test_dataset_array
from BSRM import basic_stable_roommate_matching
import random
from datetime import datetime


def random_complete_test_data(data_size=200):

    test_data = []

    for i in range(1, data_size + 1):
        tmp = []
        size_j = data_size + 1
        for j in range(1, size_j):
            if i != j:
                tmp.append(j)

        random.shuffle(tmp)
        test_data.append(tmp)

    return test_data


def batch_test(count=200, data_size=200):

    count_list = [0 for i in range(5)]

    for round in range(count):

        test_data = random_complete_test_data(data_size)

        print(round)
        print("preferences", test_data)
        type, msg, result = basic_stable_roommate_matching(test_data)
        count_list[type] = count_list[type] + 1
        print(msg, result)
        print()

        if msg == "bug":
            break

    summary = {'bug': count_list[0],
               'after phase_1 find answer': count_list[1],
               'unsolvable by phase_1': count_list[2],
               'after phase_2 find answer': count_list[3],
               'unsolvable by phase_2': count_list[4]}
    print(summary)


if __name__ == '__main__':


    batch_test(count=200, data_size=5)
    # batch_test(1, 5)

    # test_data = test_dataset_array.test_match_5
    #
    # type, msg, result = basic_stable_roommate_matching(test_data)
    #
    # print(type, msg, result)