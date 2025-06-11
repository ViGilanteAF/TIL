import sys
input = sys.stdin.readline

n = int(input())

for i in range(n, -1, -1):
    if set(str(i)).issubset({'4','7'}):
        print(i)
        break