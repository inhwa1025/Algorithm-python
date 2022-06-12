# 백준 11727번 2×n 타일링 2
# 동적계획법
n = int(input())
cache = [1, 3]


def tiling(num):
    if num <= len(cache):
        return cache[num-1]
    left = tiling(num-1)
    right = 2 * tiling(num-2)
    cache.append((left+right) % 10007)
    return cache[num-1]


print(tiling(n))
