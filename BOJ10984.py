
T = int(input())


for i in range(T):
    N = int(input())
    su = 0
    gpa = 0
    for j in range(N):
        a, b = map(float, input().split())
        su += a
        gpa += a*b
    avg = gpa/su
    print('%d %.2f' % (su, avg))  # 자바, C 같이 ',' 쉼표 찍지 말자!
