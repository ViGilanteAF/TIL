import sys
input = sys.stdin.readline
# N: 여학생 M: 남학생 K: 인턴쉽
N, M, K = map(int, input().split())
team = 0
while True:
    # 인턴쉽 참여 학생보다 남은 학생수가 적을 경우
    if N-2 + M-1 < K or N < 2 or M < 1:
        break
    if N >= 2 and M >= 1:
        team += 1
        N -= 2
        M -= 1

print(team)
