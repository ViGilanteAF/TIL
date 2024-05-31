a, b = map(str, input().split())

a = a[::-1]
b = b[::-1]

if a > b:
    print(a)
elif a < b:
    print(b)
