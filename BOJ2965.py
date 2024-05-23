import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())

range1 = b - a - 1
range2 = c - b - 1

print(max(range1, range2))
