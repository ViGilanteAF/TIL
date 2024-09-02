t = int(input())

for i in range(t):
    n = list(map(int, input().split()))

    #n 에 저장된 list 배열 중 첫번째 부터 마지막까지 더한뒤 0번째 에 있는 수로 나눈 걸 avg에 저장
    avg = sum(n[1:])/n[0]

    cnt = 0
    #j에 n배열의 첫번째 인덱스 부터 마지막의 인덱스 를 할당하여 반복
    for j in n[1:]:
        # j 에 들어오는 수가 avg에 수에 비해서 클경우
        if j > avg:
            # cnt 로 해당 인원을 증가함
            cnt += 1
    # 비율을 per 에 저장
    per = (cnt/n[0])*100
    #소수점 3자리 수 까지 반올림
    print('%.3f'%per+'%')
