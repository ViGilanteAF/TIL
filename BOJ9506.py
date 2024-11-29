import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        break

    ans = []        # n 이 아닌 약수들의 합이 n과 같으면 완전수 로 6=1+2+3 의 형태로 출력
    for i in range(1, n):
        if n % i == 0:
            ans.append(i)

    if n == sum(ans):
        #여러 값을 출력을 위해 int형이 아닌 str형 으로 출력
        #print()함수 내에 , 를 사용하면 공백이 추가가 되지만 + 를 사용하여 공백 없이 연결
        #ans 의 값을 출력하되, 숫자 사이에 + 를 넣어야 하기 때문에 "".join()을 이용
        print(str(n), "=", " + ".join(str(a) for a in ans))
    else:
        #
        print(str(n), "is NOT perfect.")