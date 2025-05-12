import sys
from collections import deque
input = sys.stdin.readline

#그래프 데이터를 담는 방법 -> 인접행렬, 인접리스트, 엣지리스트

# 인접 행렬로 담기 = 이차원 배열로 데이터 담기
n = int(input())
m = int(input())

count = [False] * (n+1)
q = [[]for _ in range(n+1)]

#BFS => FIFO => QUEUE

for _ in range(m):
    a,b = map(int, input().split())
    q[a].append(b)
    q[b].append(a)
    q[a].sort()
    q[b].sort()

se = deque([1])
cnt = 0

while se:
    v = se.popleft()
    count[v] = True
    for i in q[v]:
        if not count[i]:
            count[i] = True
            se.append(i)
            cnt += 1
print(cnt)









