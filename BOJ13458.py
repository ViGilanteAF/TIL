n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

# 총감독관은 무조건 시험장당 1명
# n = 시험장
# a = 각 시험장마다 시험응시생수
# b, c = 총감독관, 부감독관 들의 감시가능한 응시생수
count = n
for i in range(n):
    if (a[i] > b):
        count += int((a[i] - b) / c)  # int 로 묶어 주지 않으면 0.5 의 소수가 발생해서 최종 값이 바뀜
        if ((a[i] - b) % c != 0):
            count += 1

print(count)

'''

방의 갯수 =  총 감독관의 수
총감독관의 수 보다 응시생의 수가 많아야 보조감독관이 필요하게 됨
(응시생 - 총감독관 수)  / 보조감독관 
나머지 가 있을 수 있으니 나머지 가 발생시 보조감독관 +1

모두 구해서 count 출력
'''
