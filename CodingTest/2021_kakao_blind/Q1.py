def solution(new_id):
    answer = ''

    # step1
    answer = new_id.lower()

    # step2
    ascii_list = [45, 46, 95] + [i for i in range(48, 58)] + [j for j in range(97, 123)]
    for each in answer:
        asci = ord(each)
        if asci not in ascii_list:
            answer = answer.replace(each, "")

    # step3
    a = "abccd"
    i = 0
    while i < len(answer) - 1:
        if answer[i] == '.':
            for j in range(i + 1, len(answer)):
                if answer[j] != '.':
                    answer = answer[:i + 1] + answer[j:]
                    break
                if j == (len(answer) - 1):
                    answer = answer[:i + 1]
        i += 1
    del i

    # step4
    answer = answer.strip('.')

    # step5
    if answer == "":
        answer = "a"

    # step6
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.rstrip('.')

    # step7
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]

    return answer