# 프로그래머스 - 타겟 넘버
# DFS/BFS

# 재귀 사용
def solution(numbers, target):
    answer = 0

    def recursion(nums, target, result):
        nonlocal answer

        if not nums:
            if result == target:
                answer += 1
                return 0
            else:
                return 0

        recursion(nums[1:], target, result - nums[0])
        recursion(nums[1:], target, result + nums[0])

    recursion(numbers, target, 0)

    return answer


# 스택 사용
def solution1(numbers, target):
    answer = 0
    stack = [[numbers[0], 0], [-numbers[0], 0]]

    while stack:
        now, idx = stack.pop()
        if idx == len(numbers) - 1:
            if now == target:
                answer += 1
        else:
            idx += 1
            stack.append([now + numbers[idx], idx])
            stack.append([now - numbers[idx], idx])

    return answer
