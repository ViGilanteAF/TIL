import sys
input = sys.stdin.readline

N = int(input())
r, e, c = map(int, input().split())

for i in range(N):
    if r < e-c:
        print("advertise")
    elif r == e - c:
        print("dose not matter")
    else:
        print("do not advertise")
