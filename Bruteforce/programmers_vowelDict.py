# A, E, I, O, U 전체 경우의 수 5*5*5*5*5 + 5*5*5*5 + 5*5*5 + 5*5 + 5 = 3905
# "A", "AA", "AAA", "AAAA", "AAAAA"
# "AAAAE", "AAAAI", "AAAAO", "AAAAU"
# "AAAE", "AAAEA", "AAAEE", "AAAEI", "AAAEO", "AAAEU"
# ...
from itertools import permutations


# bruteforce
def solution2(word):
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


# 수학적 규칙 찾아서 푼 풀이 - 등비급수 사용
# (a-1) * ( pow(5,4) + (pow(5,4)-1)/(5-1) )
# + (b-1) * ( pow(5,3) + (pow(5,3)-1)/(5-1) )
# + (c-1) * ( pow(5,2) + (pow(5,2)-1)/(5-1) )
# + (d-1) * ( pow(5,1) + (pow(5,1)-1)/(5-1) )
# + (e-1) * ( pow(5,0) + (pow(5,0)-1)/(5-1) )
# + n
def solution(word):
    dic = {"A": 1, "E": 2, "I": 3, "O": 4, "U": 5}
    n = len(word)
    num_list = []
    result = 0

    for w in word:
        num_list.append(dic[w])
    # print(num_list)

    for i in range(n):
        result += (num_list[i] - 1) * (pow(5, 4 - i) + (pow(5, 4 - i) - 1) / 4)

    result += n

    return result
