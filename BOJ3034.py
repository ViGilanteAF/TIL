import sys
input = sys.stdin.readline

n, w, h = map(int, input().split())

size = w*w + h*h

for _ in range(n):
    temp = int(input())
    a_size = temp*temp
    if size < a_size:
        print("NE")
    else:
        print("DA")
