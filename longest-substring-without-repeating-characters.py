"""
Runtime: 1889 ms. (off-the-chart slow, dreadful)
"""

import timeit

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        smax = ""
        #for ilen in range(len(s),0,-1):
        for ilen in range(100,0,-1):
            offset = 0
            while offset + ilen <= len(s):
                subst = s[offset:ilen+offset]
                print(subst)
                if len(set(subst)) == len(subst):
                    smax = subst
                    break
                offset += 1
            if smax:
                break
        #print(smax)
        print(len(smax))
        return len(smax)

s = Solution()
if 0:
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("bbbbb") == 1
    assert s.lengthOfLongestSubstring("pwwkew") == 3
    tc0 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    assert s.lengthOfLongestSubstring(tc0) == 95
tc1 = "\"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
assert s.lengthOfLongestSubstring(tc1) == 95
#print(timeit.timeit("assert s.lengthOfLongestSubstring(tc1) == 95",number=1,globals=globals()))
print("OK")