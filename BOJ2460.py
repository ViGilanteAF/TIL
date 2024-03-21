import sys
input = sys.stdin.readline

MAX = 0
NOW = 0
for i in range(10):
    A, B = map(int, input().split())
    NOW += B-A
    if NOW > MAX:
        MAX = NOW

print(MAX)
