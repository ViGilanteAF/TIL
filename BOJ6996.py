import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())

for i in range(n):
    a, b = list(map(str, input().split()))

    if Counter(a) == Counter(b):
        print(a, '&', b, 'are anagrams.')
    else:
        print(a, '&', b, 'are NOT anagrams.')