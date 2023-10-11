'''

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
