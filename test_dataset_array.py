# from http://www.dcs.gla.ac.uk/~pat/jchoco/roommates/papers/Comp_sdarticle.pdf
paper_matching_6 = [
        [4, 6, 2, 5, 3],
        [6, 3, 5, 1, 4],
        [4, 5, 1, 6, 2],
        [2, 6, 5, 1, 3],
        [4, 2, 3, 6, 1],
        [5, 1, 4, 2, 3]
    ]

paper_matching_8 = [
        [2, 5, 4, 6, 7, 8, 3],
        [3, 6, 1, 7, 8, 5, 4],
        [4, 7, 2, 8, 5, 6, 1],
        [1, 8, 3, 5, 6, 7, 2],
        [6, 1, 8, 2, 3, 4, 7],
        [7, 2, 5, 3, 4, 1, 8],
        [8, 3, 6, 4, 1, 2, 5],
        [5, 4, 7, 1, 2, 3, 6]
    ]

paper_no_matching_4 = [
        [2, 3, 4],
        [3, 1, 4],
        [1, 2, 4],
        [1, 2, 3]
    ]

paper_no_matching_6 = [
        [2, 6, 4, 3, 5],
        [3, 5, 1, 6, 4],
        [1, 6, 2, 5, 4],
        [5, 2, 3, 6, 1],
        [6, 1, 3, 4, 2],
        [4, 2, 5, 1, 3]
    ]

# from https://en.wikipedia.org/wiki/Stable_roommates_problem#Algorithm
wiki_matching_6 = [
        [3, 4, 2, 6, 5],
        [6, 5, 4, 1, 3],
        [2, 4, 5, 1, 6],
        [5, 2, 3, 6, 1],
        [3, 1, 2, 4, 6],
        [5, 1, 3, 4, 2]
    ]

# from http://www.dcs.gla.ac.uk/~pat/roommates/distribution/data/
external_matching_8 = [
        [2, 5, 4, 6, 7, 8, 3],
        [3, 6, 1, 7, 8, 5, 4],
        [4, 7, 2, 8, 5, 6, 1],
        [1, 8, 3, 5, 6, 7, 2],
        [6, 1, 8, 2, 3, 4, 7],
        [7, 2, 5, 3, 4, 1, 8],
        [8, 3, 6, 4, 1, 2, 5],
        [5, 4, 7, 1, 2, 3, 6]
    ]

external_matching_10 = [
        [8, 2, 9, 3, 6, 4, 5, 7, 10],
        [4, 3, 8, 9, 5, 1, 10, 6, 7],
        [5, 6, 8, 2, 1, 7, 10, 4, 9],
        [10, 7, 9, 3, 1, 6, 2, 5, 8],
        [7, 4, 10, 8, 2, 6, 3, 1, 9],
        [2, 8, 7, 3, 4, 10, 1, 5, 9],
        [2, 1, 8, 3, 5, 10, 4, 6, 9],
        [10, 4, 2, 5, 6, 7, 1, 3, 9],
        [6, 7, 2, 5, 10, 3, 4, 8, 1],
        [3, 1, 6, 5, 2, 9, 8, 4, 7]
    ]

external_matching_20 = [
        [13, 12, 20, 17, 11, 6, 8, 2, 3, 14, 4, 16, 5, 10, 18, 19, 9, 15, 7],
        [13, 6, 8, 17, 18, 19, 1, 11, 7, 4, 15, 16, 5, 9, 3, 20, 12, 10, 14],
        [6, 16, 4, 9, 14, 13, 17, 19, 8, 2, 1, 12, 20, 5, 18, 15, 7, 11, 10],
        [11, 7, 8, 2, 17, 3, 15, 6, 19, 10, 9, 5, 1, 16, 13, 20, 18, 14, 12],
        [8, 17, 14, 16, 4, 13, 15, 6, 19, 9, 12, 7, 2, 3, 11, 18, 20, 10, 1],
        [8, 13, 10, 14, 18, 15, 2, 7, 4, 16, 19, 5, 9, 17, 20, 3, 11, 12, 1],
        [13, 1, 4, 9, 19, 18, 11, 14, 10, 2, 17, 6, 15, 16, 5, 3, 12, 8, 20],
        [1, 6, 20, 7, 5, 15, 19, 4, 12, 3, 17, 9, 10, 14, 16, 2, 18, 11, 13],
        [17, 13, 3, 5, 7, 4, 12, 2, 18, 20, 15, 8, 10, 1, 6, 11, 19, 14, 16],
        [9, 4, 16, 14, 18, 17, 15, 11, 20, 13, 3, 12, 2, 1, 19, 7, 5, 8, 6],
        [6, 15, 4, 1, 18, 14, 5, 3, 9, 2, 17, 13, 8, 7, 12, 20, 19, 10, 16],
        [5, 18, 7, 16, 6, 20, 19, 14, 9, 17, 3, 1, 8, 10, 11, 13, 2, 15, 4],
        [3, 10, 7, 18, 14, 15, 1, 6, 12, 4, 8, 19, 16, 17, 5, 20, 9, 11, 2],
        [2, 5, 10, 13, 19, 17, 6, 3, 18, 7, 20, 9, 1, 4, 16, 12, 15, 8, 11],
        [12, 13, 5, 11, 2, 16, 18, 14, 1, 6, 17, 8, 19, 4, 10, 7, 20, 3, 9],
        [1, 7, 6, 5, 14, 18, 12, 17, 20, 11, 15, 10, 2, 13, 3, 8, 19, 9, 4],
        [5, 8, 15, 9, 7, 18, 11, 10, 19, 2, 1, 12, 3, 14, 20, 13, 6, 16, 4],
        [14, 3, 8, 10, 13, 5, 9, 15, 12, 1, 17, 6, 16, 11, 2, 7, 4, 19, 20],
        [9, 15, 20, 12, 18, 1, 11, 5, 3, 2, 13, 14, 10, 7, 6, 16, 8, 17, 4],
        [5, 6, 18, 19, 16, 7, 4, 9, 2, 17, 8, 15, 1, 12, 13, 10, 14, 3, 11]
    ]


# matching exists if algorithm leaves 7 unmatched
external_matching_7 = [
        [3, 4, 2, 6, 5, 7],
        [6, 5, 4, 1, 3, 7],
        [2, 4, 5, 1, 6, 7],
        [5, 2, 3, 6, 1, 7],
        [3, 1, 2, 4, 6, 7],
        [5, 1, 3, 4, 2, 7],
        [1, 2, 3, 4, 5, 6]
    ]


# custom test cases
# empty matrix
custom_no_matching_empty = []

# one person (no matching should be possible)
custom_no_matching_1 = [[]]

# two people
custom_matching_2 = [[2], [1]]

# three people (odd: should add person and find a matching)
custom_matching_3 = [
        [3, 2],
        [3, 1],
        [1, 2]
    ]

test_match_1 = [
        [4, 2, 3],
        [1, 3, 4],
        [2, 4, 1],
        [2, 1, 3]
    ]

test_match_2 = [
        [3, 4, 2, 6, 5],
        [6, 5, 4, 1, 3],
        [2, 4, 5, 1, 6],
        [5, 2, 3, 6, 1],
        [3, 1, 2, 4, 6],
        [5, 1, 3, 4, 2]]

test_match_4 = [
        [4, 2, 6],
        [1, 6],
        [6, 4],
        [3, 1],
        [6],
        [1, 3, 5, 2]
    ]

# 这个match 5 虽然是奇数长度的列表但是在经过第一阶段不会产生空
test_match_5 = [
        [4, 3, 5, 2],
        [3, 4, 1, 5],
        [5, 2, 4, 1],
        [5, 3, 2, 1],
        [1, 3, 2, 4]
]

# 这个unsolvable by phase_1 [[5], [3, 4], [], [4, 1], [1, 3], [0]]
test_match_6 = [
        [6, 4, 3, 5, 2],
        [4, 5, 6, 1, 3],
        [2, 1, 6, 5, 4],
        [6, 1, 5, 2, 3],
        [2, 4, 1, 3, 6],
        [2, 1, 3, 5, 4]
]

