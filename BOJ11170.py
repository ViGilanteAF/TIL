import sys
input = sys.stdin.readline

T = int(input())

k = 0
for i in range(T):
    n, m = map(int, input().split())
    for a in range(n, m+1):
       k += str(a).count('0')
    print(k)
    k = 0