import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    word = input().split()
    for j in word:
        print(j[::-1], end=' ')

