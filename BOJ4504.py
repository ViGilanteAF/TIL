import sys
input = sys.stdin.readline

n = int(input())

while (True):
    now = int(input())
    if now == 0:
        break
    if (now % n == 0):
        print(str(now) + " is a multiple of " + str(n) + ".")
    else:
        print(str(now) + " is NOT a multiple of " + str(n) + ".")
