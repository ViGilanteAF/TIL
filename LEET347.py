'''
heap에 원소를 다 넣을때 까지 heap[0]을 접근하거나 heappush, heappop을 할 일이 없어서 append로 다 넣고 난뒤
heapify로 힙의 조건을 만족하게 원소들을 재배치 하는것
'''
from heapq import heapify, heappop
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num2cout = Counter(nums)
        heap = []
        for num, count in num2cout.items():
            heap.append((-count, num))
        heapify(heap)
        answer = []
        for _ in range(k):
            _, num = heappop(heap)
            answer.append(num)
        return answer
