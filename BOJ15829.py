l = int(input())
num = list(input())
r = 31
m = 1234567891
rst = 0

for i in range(l):
    v = ord(num[i]) - 96
    a = r**i
    rst += v * a

print(rst % m)
