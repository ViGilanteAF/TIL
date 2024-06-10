
a = []
b = 0
for i in range(5):
    n = int(input())
    a.append(n)
    b += a[i]


print(int(b/5))
a.sort()
print(a[int(len(a)/2)])
