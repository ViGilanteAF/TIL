import sys

input = sys.stdin.readline

m = []
n = input()

for i in range(int(n)):
    a, b = input().rstrip().split()
    m.append((int(a), b))

m.sort(key=lambda x: x[0])

for j in m:
    print(j[0], j[1])


