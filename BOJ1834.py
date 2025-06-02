import sys
input = sys.stdin.readline

n = int(input())
m = 0
for i in range(1,n):
    tmp = n * i + i
    m += tmp

print(m)