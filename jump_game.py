"""
unsolved so far!
"""

class Solution:
    def __init__(self):
        self.steps = 0
    
    def canJump(self, nums):
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+n)
        return True


    def canJumpSlow(self, nums):
        #print(nums) #REMOVE
        self.steps +=1
        #print(self.steps) #REMOVE

        if len(nums) == 0:
            return False
        if len(nums) == 1:
            self.steps = 0
            return True
        if nums[0] == 0:
            return False
        jumps = list(range(1, nums[0]+1))
        for j in jumps[::-1]:
            print(nums[:j+1])
            ret = self.canJump(nums[j:])
            if ret == True:
                return True
        return False

    def canJump_yuck(self, nums):
        def index_right(l0, value):
            return len(l0) - l0[::-1].index(value) - 1
        idx = 0
        while idx < len(nums)-1:
            next_nums = nums[idx+1:idx+nums[idx]+1]
            #print(next_nums)
            hi = max(next_nums)
            nn = index_right(next_nums, hi) 
            temp = idx + nn +1
            while nums[temp] == 0:
                temp+=1 #we have to reach it or game over
            avail = nums[max(temp-9,0):temp+1]
            #print(avail)
            if 0 in avail:
                able = [x-(len(avail[:-avail.index(0)])-1 - i) for i,x in enumerate(avail[:-avail.index(0)])]
                #able = [x-(len(nums)-1 - i) for i,x in enumerate(nums[:-(avail.index(0)-1)])]
                print(able)
                if any([x>=0 for x in able]):
                    maxable = max(able)
                    temp += index_right(able, maxable)
                else:
                    print("bad")
                    return False

            idx = int(temp)
        print("good")
        return True

s = Solution()

assert s.canJump([2,3,1,1,4]) == True
if 0:
    
    assert s.canJump([3,2,1,0,4]) == False
    assert s.canJump([4,4]) == True

    l0 = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    assert s.canJump(l0) == False
print("All OK")
