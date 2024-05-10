import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    temp = list(map(int, input().split()))
    sum = 0
    for j in range(n):
        sum += temp[j]
    print(sum)
