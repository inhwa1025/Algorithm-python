# Codility 4-3. MissingInteger

def solution(A):
    A.sort()
    result = 1
    for a in A:
        if result == a:
            result += 1
        elif result < a:
            break
    return result
