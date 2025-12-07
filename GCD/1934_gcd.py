# 최소공배수 구하기
# 유클리드호제법 사용

t = int(input())

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

for i in range(t):
    a,b = map(int, input().split())
    result = a * b // gcd(a,b)
    print(int(result))