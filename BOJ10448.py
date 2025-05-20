import sys

input = sys.stdin.readline

T = [u * (u + 1) // 2 for u in range(1, 46)]

sam = [0]*1001

for _ in range(int(input())):
    ko = int(input())
    for i in T:
        for j in T:
            for k in T:
                if i+j+k <= 1000:
                    sam[i+j+k] = 1
    print(sam[ko])
