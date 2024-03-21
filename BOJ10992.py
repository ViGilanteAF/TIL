import sys
print = sys.stdout.write
N = int(input())

for i in range(N):
    for j in range(N+i):
        if i == 0:
            if j == N-1:
                print("*")
            else:
                print(" ")
        elif i != N - 1:
            if j == N - 1 - i or j == N-1+i:
                print("*")
            else:
                print(" ")
        else:
            print("*")
    print("\n")
