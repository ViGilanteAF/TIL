import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())

for i in range(N):
    for j in range(N+i):
        if j == N-i-1 or j == N+i-1:
            print("*")
        else:
            print(" ")
    print("\n")
