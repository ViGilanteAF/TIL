import sys

input = sys.stdin.readline

n = int(input())
check = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
move = 0
for i in range(n):
    a, b = map(int, input().split())

    if check[a] != -1 and check[a] != b:
        move += 1

    check[a] = b

print(move)