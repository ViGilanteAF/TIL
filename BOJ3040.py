num = []
sum = 0
for _ in range(9):
    n = int(input())
    num.append(n)
    sum = sum + n

for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if sum - num[i] - num[j] == 100:  #입력받은 수 중에서 2개를 뺀 나머지 수들의 합이 100인 경우 그 나머지수들이 답
            for k in range(len(num)):
                if k != i and k != j: #그러면 나머지 수 를 출력하면 된다.
                    print(num[k])
            break #답을 찾았기 때문에 break를 걸어서 for문을 종료함
