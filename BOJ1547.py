# 컵을 움직이는게 아니라 공을 움직이는거임 공의 위치 = 컵의 위치
import sys
input = sys.stdin.readline

N = int(input())
# 컵은 3개 이지만 0부터 시작 하는 List 로 인해서 그냥 1부터 시작하게끔 함
A = [0, 1, 0, 0]
for _ in range(N):
    X, Y = map(int, input().split())
    temp = A[X]
    A[X] = A[Y]
    A[Y] = temp

for i in range(1, 4):
    if A[i] == 1:
        print(i)
        break
