import sys
input = sys.stdin.readline

N = int(input())
A = 100
B = 100

for i in range(N):
    C, D = map(int, input().split())
    if C > D:
        B -= C
    elif D > C:
        A -= D
print(A)
print(B)
