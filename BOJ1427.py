import sys

input = sys.stdin.readline

n = input()
m = sorted(n, reverse=True)
result = ''.join(m)
print(result)
