n = int(input())
a = []
for i in range(n):
    b = int(input())
    a.append(b)
    a.sort()

for i in a:
    print(i)

'''
입력
4
2
3
4
1

출력
1
2
3
4
5
'''
