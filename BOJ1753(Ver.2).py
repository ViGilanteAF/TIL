import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
v, e = map(int, input().split())

# 시작점
K = int(input())

# 가중치 테이블dp
dp = [INF]*(v+1)
heap = []
graph = [[] for _ in range(v+1)]


def dj(start):
    # 가중치 테입르에서 시작지점에 해당하는 가중리를 0으로 초기화함
    dp[start] = 0
    heapq.heappush(heap, (0, start))

    # 힙에 원소가 없을 때 까지 반복
    while heap:
        wei, now = heapq.heappop(heap)

        # 현재 테이블과 비교하여 불필요한(가중치가 더큰) 튜플이면 무시
        if dp[now] < wei:
            continue

        for w, next_node in graph[now]:
            # 현재 정점까지 의 가중치 wei + 현재 정점에서 다음 정점(next_node)까지의 가중치 W = 다음 노드까지의 가중치(next_wei)
            next_wei = w + wei

            # 다음 노드까지의 가중치(next_wei) 가 현재 기록되어있는 값 보다 작으면
            if next_wei < dp[next_node]:

                # 계산했던 next_wei를 가중치 테이블 에 업데이트
                dp[next_node] = next_wei

                # 다음 점 까지의 가중치와 다음 점에 대한 정보를 튜플로 합쳐 최소 힙에 삽입
                heapq.heappush(heap, (next_wei, next_node))


# 초기화
'''
변수명은 필드가 달라도 꼭 다르게 쓰자 되도록이면 소문자, 대문자 말고
뒤에 1,2,3 을 붙이는 변수명 으로!!!!

밑에 for 문에 서 선언된 u, v1, w 이 3개 변수중 v 변수가 위에 dj함수 내에서 사용되는
v 변수와 변수명이 같아서 마지막 INF 를 나타내는 힙을 한번 돌지 않는 원치않은 결과가 자꾸 나와서 
문제에서 틀렸다고 출력이 되었다!
'''
for _ in range(e):
    u, v1, w = map(int, input().split())
    # 가중치, 목적지노드 형태로 저장
    graph[u].append((w, v1))

dj(K)
for i in range(1, v+1):
    print("INF" if dp[i] == INF else dp[i])
