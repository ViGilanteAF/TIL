
# 0 = 4cm, 1 = 2cm, other = 3cm
size = [4, 2, 3, 3, 3, 3, 3, 3, 3, 3]

while True:
    num = input()
    if int(num) == 0:
        break

    ans = len(num) + 1
    for i in num:
        idx = int(i)
        ans += size[idx]
    print(ans)

'''
import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '0':
        break
    
    ans = 2 + len(s) - 1
    for i in s:
        if i == '1':
            ans += 2
        elif i == '0':
            ans += 4
        else:
            ans += 3
    print(ans)
'''
