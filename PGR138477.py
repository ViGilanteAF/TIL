'''
원소를 다 넣기 전에도 각각의 for-loop 안에 조건을 만족해야 하기 때문에 
heappush로 넣는것
append 가 아닌 heappush를 쓰게 되면 조건을 만족하돌록 파이썬에서 적절한 위치에 넣어주는것!
'''

from heapq import heapify, heappop, heappush


def solution(k, score):
    answer = []
    heap = []
    for s in score:
        if len(heap) < k:
            heappush(heap, s)
        elif heap[0] < s:
            heappop(heap)
            heappush(heap, s)
        answer.append(heap[0])
    return answer
