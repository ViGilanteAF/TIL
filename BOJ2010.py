import sys
input = sys.stdin.readline

N = int(input())
sum = 0

for i in range(N):
    sum += int(input())

print(sum - (N - 1))
