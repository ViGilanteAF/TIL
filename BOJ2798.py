n, m = map(int, input().split())
a = list(map(int, input().split()))

max = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            tmp = a[i] + a[j] + a[k]
            if (max < tmp and m >= tmp):
                max = tmp

print(max)
