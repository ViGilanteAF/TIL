import sys
input = sys.stdin.readline

n = list(map(int, input().split()))
m = len(n)
for i in range(m):
    for j in range(0, m - i -1):
        if n[j] > n[j + 1]:
            n[j], n[j + 1] = n[j + 1], n[j]
            print(*n)

