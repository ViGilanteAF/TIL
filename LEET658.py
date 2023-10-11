from heapq import heapify, heappush, heappop


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = [(abs(x-el), el)for el in arr]
        heapify(heap)
        answer = []
        for _ in range(k):
            _, el = heappop(heap)
            answer.append(el)
        return sorted(answer)
