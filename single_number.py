"""
Runtime: 197 ms. Your runtime beats 48.32 % of python3 submissions.
"""
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cand = set()
        for n in nums:
            if n in cand:
                cand.remove(n)
            else:
                cand.add(n)
        return cand.pop()

s = Solution()
assert s.singleNumber([2,2,1]) == 1
assert s.singleNumber([4,1,2,1,2]) == 4
assert s.singleNumber([1]) == 1
print("All OK")
