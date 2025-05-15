import sys
input = sys.stdin.readline
max = 0


for _ in range(int(input())):
    for _ in range(int(input())):
        s,l = map(str, input().split())
        if max < int(l):
            max = int(l)
            name = s

    print(name)