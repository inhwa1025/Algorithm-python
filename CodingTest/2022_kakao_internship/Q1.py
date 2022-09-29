def solution(survey, choices):
    answer = ''
    result = [[0, 0] for _ in range(4)]
    # [[R, T], [C, F], [J, M], [A, N]]

    for i in range(len(survey)):
        s = survey[i][0]    # i번째 응답의 첫글자
        choice = choices[i]

        if s == "R":        # RT
            if choice < 4:  # R
                result[0][0] += (4 - choice)
            elif choice > 4: # T
                result[0][1] += (choice - 4)
        elif s == "T":      # TR
            if choice < 4:  # T
                result[0][1] += (4 - choice)
            elif choice > 4: # R
                result[0][0] += (choice - 4)
        elif s == "C":      # CF
            if choice < 4:  # C
                result[1][0] += (4 - choice)
            elif choice > 4: # F
                result[1][1] += (choice - 4)
        elif s == "F":      # FC
            if choice < 4:  # F
                result[1][1] += (4 - choice)
            elif choice > 4: # C
                result[1][0] += (choice - 4)
        elif s == "J":      # JM
            if choice < 4:  # J
                result[2][0] += (4 - choice)
            elif choice > 4: # M
                result[2][1] += (choice - 4)
        elif s == "M":      # MJ
            if choice < 4:  # M
                result[2][1] += (4 - choice)
            elif choice > 4: # J
                result[2][0] += (choice - 4)
        elif s == "A":      # AN
            if choice < 4:  # A
                result[3][0] += (4 - choice)
            elif choice > 4: # N
                result[3][1] += (choice - 4)
        else:               # NA
            if choice < 4:  # N
                result[3][1] += (4 - choice)
            elif choice > 4: # A
                result[3][0] += (choice - 4)

    if result[0][0] < result[0][1]:
        answer += 'T'
    else:
        answer += 'R'
    if result[1][0] < result[1][1]:
        answer += 'F'
    else:
        answer += 'C'
    if result[2][0] < result[2][1]:
        answer += 'M'
    else:
        answer += 'J'
    if result[3][0] < result[3][1]:
        answer += 'N'
    else:
        answer += 'A'

    return answer