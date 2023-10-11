'''
array words 와 k개가 주어졌을때
k개의 가장 frequent한, 가장 자주 나오는 string을 return 해야 한다.
'''

'''
오름차순을 frequenecy 에 해야하고 가장 빈도수가 높은것부터
빈도수가 같다면 사전순으로 먼저 나와야 함
'''

from heapq import heapify, heappush, heapify
from collections import Counter

class Solution:
    def topKFrequent (self, wordsL List[str], k:int) -> List[str]:
        word2count = Counter(words)
        heap = []
        for word, count in word2count.items():
            heap.append((-count, word))
        heapify(heap)
        answer  = []
        for _ in range(k):
            _, word = heappop(heap)
            answer.append(word)
        return answer