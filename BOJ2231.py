n = int(input())
result = 0


for i in range(1, n+1):
    if i == n:
        print(0)
        break
    nums = list(map(int, str(i)))
    result = sum(nums) + i
    if result == n:
        print(i)
        break
