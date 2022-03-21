from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return set(range(len(nums)+1)).difference(set(nums)).pop()

s = Solution()
assert s.missingNumber([3,0,1]) == 2
assert s.missingNumber([0,1]) == 2
assert s.missingNumber([9,6,4,2,3,5,7,0,1]) == 8
print("All OK")
