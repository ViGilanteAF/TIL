# swap 하는것에 대하여 알아보는 문제
n, m = map(int, input().split())
# a = [i for i in range(1, n+1)]

a = []
for i in range(1, n+1):
    a.append(i)


for i in range(m):
    s, e = map(int, input().split())
    temp = a[s-1:e]
    temp.reverse()
    a[s-1:e] = temp


for i in range(n):
    print(a[i], end=' ')
