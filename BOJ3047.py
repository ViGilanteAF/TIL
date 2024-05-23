abc = list(map(int, input().split()))
abc.sort()

order = input()

for i in order:
    if i == 'A':
        print(abc[0], end=' ')
    elif i == 'B':
        print(abc[1], end=' ')
    else:
        print(abc[2], end=' ')
