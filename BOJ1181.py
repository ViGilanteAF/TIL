import sys
# input = sys.stdin.readline

n = int(input())
arr = [set() for _ in range(20001)]
for _ in range(n):
    a = input()
    arr[len(a)].add(a)
for i in range(20001):
    for j in sorted(arr[i]):
        print(j)