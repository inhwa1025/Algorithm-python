def L_or_R(left_distance, right_distance, hand):
    if left_distance < right_distance:
        return "L"
    elif left_distance > right_distance:
        return "R"
    else:
        if hand == "left":
            return "L"
        else:
            return "R"


def solution(numbers, hand):
    answer = ''
    right = [3, 2]
    left = [3, 0]

    for num in numbers:
        if num == 1:
            left = [0, 0]
            answer += "L"
        elif num == 4:
            left = [1, 0]
            answer += "L"
        elif num == 7:
            left = [2, 0]
            answer += "L"
        elif num == 3:
            right = [0, 2]
            answer += "R"
        elif num == 6:
            right = [1, 2]
            answer += "R"
        elif num == 9:
            right = [2, 2]
            answer += "R"
        elif num == 2:
            result = L_or_R(abs(left[0] - 0) + abs(left[1] - 1),
                            abs(right[0] - 0) + abs(right[1] - 1),
                            hand)
            answer += result
            if result == "L":
                left = [0, 1]
            else:
                right = [0, 1]
        elif num == 5:
            result = L_or_R(abs(left[0] - 1) + abs(left[1] - 1),
                            abs(right[0] - 1) + abs(right[1] - 1),
                            hand)
            answer += result
            if result == "L":
                left = [1, 1]
            else:
                right = [1, 1]
        elif num == 8:
            result = L_or_R(abs(left[0] - 2) + abs(left[1] - 1),
                            abs(right[0] - 2) + abs(right[1] - 1),
                            hand)
            answer += result
            if result == "L":
                left = [2, 1]
            else:
                right = [2, 1]
        elif num == 0:
            result = L_or_R(abs(left[0] - 3) + abs(left[1] - 1),
                            abs(right[0] - 3) + abs(right[1] - 1),
                            hand)
            answer += result
            if result == "L":
                left = [3, 1]
            else:
                right = [3, 1]

    return answer