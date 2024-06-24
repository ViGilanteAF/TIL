import math

m = int(input())
n = int(input())
tmp = []
for i in range(m, n+1):
    if int(math.sqrt(i)) ** 2 == i:
        tmp.append(i)

if (tmp):
    print(sum(tmp))
    print(min(tmp))

else:
    print(-1)
