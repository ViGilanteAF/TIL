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
