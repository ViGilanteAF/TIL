# Permutation
from itertools import permutations


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(prefix, nums):
            if not nums:
                yield prefix
                return
            for idx, num in enumerate(nums):
                yield from helper(prefix + [num], nums[:idx] + nums[idx+1:])
        return list(helper([], nums))
