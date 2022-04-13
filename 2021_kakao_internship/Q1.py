import sys

s = str(sys.stdin.readline().strip())
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

print(int(result))
