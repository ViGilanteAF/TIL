import sys

input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
now = m[0] #한조 높이
kill = 0 #한조 처치수
mxkill = 0 #한조 최대 킬수

for i in range(n):
    if m[i] < now:
        kill += 1
    else:
        now = m[i]
        if mxkill < kill:
            mxkill = kill
        kill = 0
if mxkill < kill:
    mxkill = kill

print(mxkill)