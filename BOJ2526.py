import sys
input = sys.stdin.readline

n, p = map(int, input().split())
see = []
tmp = 1
while True:
    tmp = (tmp * n) % p
    if tmp in see:
        break
    see.append(tmp)
print(len(see) - see.index(tmp))

'''
see = set()


see.add(tmp)
print(len(see))
'''