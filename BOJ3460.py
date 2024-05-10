import sys
input = sys.stdin.readline

T = int(input())
# stdout.write 으로 하면 줄바꿈이 안됨
print = sys.stdout.write

for i in range(T):
    A = []
    N = int(input())
    index = 0
    while (N > 0):
        if N % 2 == 1:
            A.append(index)
        N //= 2
        index += 1

    for j in range(len(A)):
        print(str(A[j]) + " ")
    print("\n")
