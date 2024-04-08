import sys
input = sys.stdin.readline

N = int(input())

sum = 0
count = 0
right = list(map(int, input().split()))

for _ in range(N):
    if right[_] == 1:
        count += 1
        sum += count
    else:
        count = 0
print(sum)
