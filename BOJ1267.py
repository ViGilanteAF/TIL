import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Y_A = 0
M_A = 0

for i in range(N):
    # 무조건 사용하면 기본료가 청구가 됨
    Y_A += 10
    M_A += 15
    time = A[i]

# // 몫만 활용할때 사용함
# 영식요금제 는 30초마다 10원 , 민식이는 60초마다 15원 이 과금이 된다.
    Y_A += time//30 * 10
    M_A += time//60 * 15

if Y_A == M_A:
    print("Y M " + str(Y_A))
elif Y_A < M_A:
    print("Y " + str(Y_A))
else:
    print("M " + str(M_A))
