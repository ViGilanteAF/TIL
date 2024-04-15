import sys
input = sys.stdin.readline
N = int(input())
sum = 0

for _ in range(N):
    A, B = map(int, input().split())

    sum = B % A

print(sum)
