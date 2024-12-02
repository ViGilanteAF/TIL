import sys
input = sys.stdin.readline

n, m = map(int, input().split())

t = []

for i in range(0, m+1):
    for j in range(i):
        t.append(i)

print(sum(t[n-1:m]))
