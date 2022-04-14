import sys

s = str(sys.stdin.readline().strip())


# -------혼자 푼 방법-------
def solution_1(s):
    result = ""

    while len(s) > 0:
        if s[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            result += s[0]
            s = s[1:]
        elif s[:3] == 'one':
            result += '1'
            s = s[3:]
        elif s[:3] == 'two':
            result += '2'
            s = s[3:]
        elif s[:3] == 'six':
            result += '6'
            s = s[3:]
        elif s[:4] == 'zero':
            result += '0'
            s = s[4:]
        elif s[:4] == 'four':
            result += '4'
            s = s[4:]
        elif s[:4] == 'five':
            result += '5'
            s = s[4:]
        elif s[:4] == 'nine':
            result += '9'
            s = s[4:]
        elif s[:5] == 'three':
            result += '3'
            s = s[5:]
        elif s[:5] == 'seven':
            result += '7'
            s = s[5:]
        elif s[:5] == 'eight':
            result += '8'
            s = s[5:]

    return int(result)


# -------대표 풀이-------
def solution(s):
    s = s.replace('zero', '0')
    s = s.replace('one', '1')
    s = s.replace('two', '2')
    s = s.replace('three', '3')
    s = s.replace('four', '4')
    s = s.replace('five', '5')
    s = s.replace('six', '6')
    s = s.replace('seven', '7')
    s = s.replace('eight', '8')
    s = s.replace('nine', '9')

    return int(s)


print(solution(s))
