import sys
input = sys.stdin.readline


n = input().strip()

m = int(n,2)

a = oct(m)[2:]

print(a)

