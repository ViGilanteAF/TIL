n = int(input())
a = []
for i in range(n):
    b = int(input())
    a.append(b)
    a.sort(reverse=True)

for i in a:
    print(i)

'''
입력
5
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
