t = int(input())

for _ in range(t):
    n, s = input().split()
    n = int(n)

    for a in s:
        print(a*n, end='')
    print(" ")
