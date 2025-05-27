import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
k = 0
m = 0

for i in range(1,n):
    if p[i] > p[i-1]:
        k += p[i] - p[i-1]
        if m < k:
            m = k
    else:
        k = 0

print(m)
