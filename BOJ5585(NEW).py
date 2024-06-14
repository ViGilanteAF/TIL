a = [500, 100, 50, 10, 5, 1]
n = int(input())
count = 0
s = 1000-n
for i in range(len(a)):
    count += int(s/a[i])
    s = s % a[i]

print(count)
