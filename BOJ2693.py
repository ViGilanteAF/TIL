import sys
input = sys.stdin.readline

n = [list(map(int, input().split())) for _ in range(int(input()))]

for row in n:
    row.sort()
    print(row[-3])


