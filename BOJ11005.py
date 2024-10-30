import sys

input = sys.stdin.readline

n, b = map(int, input().split())
result = ''

while n != 0:
    if n % b > 9:
        result = result + chr((n % b) + 55)
    else:
        result = result + str(n % b)
    n = n // b
print(result[::-1])
