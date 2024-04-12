import sys
input = sys.stdin.readline

N = int(input())

min_X, min_Y = map(int, input().split())

max_X = min_X
max_Y = min_Y

for i in range(N-1):
    X, Y = map(int, input().split())
    if X > max_X:
        max_X = X
    if X < min_X:
        min_X = X
    if Y > max_Y:
        max_Y = Y
    if Y < min_Y:
        min_Y = Y

print((max_X - min_X) * (max_Y - min_Y))
