n = int(input())
sum = 0

for i in range(n+1):
    for j in range(i+1):
        sum += i
        sum += j
print(sum)
