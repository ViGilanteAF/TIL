import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cnt = []
rcnt = 0
lcnt = 0
for i in range(n):
    cnt.append(input())

for j in range(n):
    if"X" not in cnt[j]:
        rcnt += 1
for k in range(m):
    if "X" not in [cnt[j][k] for j in range(n)]:
        lcnt += 1

print(max(rcnt, lcnt))
