import sys
input = sys.stdin.readline
arr = []
total = 0
first =0
second = 0

for i in range(9):
    n = int(input())
    arr.append(n)
    total = sum(arr)


for i in range(8):
    for j in range(i+1,9):
        if total - (arr[i]+arr[j]) == 100:
            first, second = arr[i], arr[j]
            break
arr.sort()
arr.remove(first)
arr.remove(second)
for x in arr:
    print(x)