import sys
input = sys.stdin.readline

x, y = map(int, input().split())

a = int(str(x)[::-1])
b = int(str(y)[::-1])

print(int(str(a+b)[::-1]))