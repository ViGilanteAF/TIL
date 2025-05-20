import sys

input = sys.stdin.readline

n = list(map(int, input().split()))
n.sort()
b = n[0]


while True:
    a = 0
    for i in range(len(n)):
        if b % n[i] == 0:
            a += 1
    if a > 2:
        print(b)
        break
    b += 1