import sys
input = sys.stdin.readline

a = 0
for _ in range(10):
    n = int(input())
    a += n
    if a > 100:
        x = a - 100
        y = 100 - (a - n)
        if y < x:
            a -= n
        break
print(a)