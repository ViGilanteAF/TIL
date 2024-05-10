import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

for i in range(N):
    for j in range(N*2):
        if (j+i) % 2 == 0:
            print("*")
        else:
            print(" ")
    print("\n")
