from collections import deque
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s0 = str(x)
        if s0[0] != s0[-1]: return False
        lp=1
        rp=len(s0)-2
        while lp<rp:
            if s0[lp] != s0[rp]:
                return False
            lp += 1
            rp -= 1
        return True

    def isPalindrome1(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]

    def isPalindrome0(self, x: int) -> bool:
        q = deque(str(x))
        while len(q)>1:
            l = q.popleft()
            r = q.pop()
            if l!=r: return False
        return True

s = Solution()

assert s.isPalindrome(121) == True
assert s.isPalindrome(-121) == False
assert s.isPalindrome(10) == False
print("All OK")
