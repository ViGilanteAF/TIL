import sys
input = sys.stdin.readline

cnt = 0
while True:
    l, p, v = map(int, input().split())
    if(l==int(0) and p==int(0) and v==int(0)):
        break
    day = int(v//p*l)
    day += min(l, v % p)
    cnt += 1
    print(f"Case {cnt}: {day}")



