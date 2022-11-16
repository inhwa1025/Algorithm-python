# A, E, I, O, U 전체 경우의 수 5*5*5*5*5 + 5*5*5*5 + 5*5*5 + 5*5 + 5 = 3905
# "A", "AA", "AAA", "AAAA", "AAAAA"
# "AAAAE", "AAAAI", "AAAAO", "AAAAU"
# "AAAE", "AAAEA", "AAAEE", "AAAEI", "AAAEO", "AAAEU"
# ...
from itertools import permutations


def solution(word):
    # dic = {"A": 1, "E": 2, "I": 3, "O": 4, "U": 5}
    arr = ["A", "A", "A", "A", "A",
           "E", "E", "E", "E", "E",
           "I", "I", "I", "I", "I",
           "O", "O", "O", "O", "O",
           "U", "U", "U", "U", "U"]
    every = set()

    for i in range(1, 6):
        every.update(list(map(''.join, permutations(arr, i))))

    every = sorted(list(every))
    # print(every)

    return every.index(word) + 1
