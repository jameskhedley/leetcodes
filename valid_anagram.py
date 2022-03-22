"""
Runtime: 48 ms. Your runtime beats 89.05 % of python3 submissions. (good!)
"""

class Solution:
    def isAnagram0(self, s: str, t: str) -> bool:
        d0 = {c: sum([x==c for x in s]) for c in set(s)}
        d1 = {c: sum([x==c for x in t]) for c in set(t)}
        return d0==d1

    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


s = Solution()
assert s.isAnagram("anagram", "nagaram")==True
assert s.isAnagram("aacc", "ccac")==False
print("All OK")
