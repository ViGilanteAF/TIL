import sys
input = sys.stdin.readline

N = int(input())
MAX = -1
for _ in range(N):
    A, B, C = map(int, input().split())
    temp = 0

    if A == B == C:
        temp = 10000 + A * 1000
    elif A == B or A == C or B == C:
        if A == B:
            temp = 1000 + A * 100
        else:
            temp = 1000 + C * 100
    else:
        temp = max(max(A, B), C) * 100
    if MAX < temp:
        MAX = temp

print(MAX)
