# 백준 10814번 나이순 정렬
# 정렬
import sys

n = int(sys.stdin.readline())
array = []

for _ in range(n):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    array.append((age, name))

array.sort(key=lambda x: x[0])

for i in array:
    print(i[0], i[1])