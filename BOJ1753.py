from queue import PriorityQueue
import sys


V, E = map(int, input().split())
K = int(input())
distance = [sys.maxsize] * (V+1)

visited = [False] * (V+1)
nearList = [[] for _ in range(V+1)]
q = PriorityQueue()

for _ in range(E):
    u, v, w = map(int, input().split())
    nearList[u].append((v, w))


q.put((0, K))  # 0을 먼저 사용한 이유는 바로 파이썬 에서는 앞에 있는 수  기준으로 배열이 정렬됨

distance[K] = 0

while q.qsize() > 0:
    current = q.get()
    c_v = current[1]
    if visited[c_v]:
        continue
    visited[c_v] = True

    for tem in nearList[c_v]:
        next = tem[0]
        value = tem[1]
        if distance[next] > distance[c_v] + value:
            distance[next] = distance[c_v] + value
            q.put((distance[next], next))

for i in range(1, V+1):
    if distance[i] != sys.maxsize:
        print(distance[1])
    else:
        print("INF")
