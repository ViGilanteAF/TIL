n = int(input())

for i in range(n):
    print("* " * (n - n // 2))
    print(" *"*(n//2))
'''
'* ' 이게 하나의 글자라고 생각하면 이해가 쉬움
n = 3 일 경우
n-n//2 의 경우 천줄에 '* ' 를 2번 찍어내라는 것이고
n//2 는 ' *' 를 1번 찍어 내라는 것이다.
'''

