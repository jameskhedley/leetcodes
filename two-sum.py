from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        snums = sorted(nums)
        found = False
        for i, n in enumerate(snums):
            for o in snums[i+1:]:
                if o + n == target:
                    found = True
                    break
                if o + n > target:
                    break
            if found:
                break
        ans0 = nums.index(n)
        nums[ans0] = -1
        ans1 = nums.index(o)
        ans = [ans0, ans1]
        print(ans)
        return ans
        

s = Solution()

if 1:
    assert s.twoSum([2,7,11,15], 9) == [0,1]
    assert s.twoSum([3,2,4], 6) == [1,2]
assert s.twoSum([3,3], 6) == [0,1]
