import sys
input = sys.stdin.readline

n = input()
arr = list(map(int, input().split()))

print(max(arr) * min(arr))
