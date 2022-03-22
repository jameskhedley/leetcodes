"""
Runtime: 74 ms. Your runtime beats 42.24 % of python3 submissions.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {"X":10,"I":1,"V":5,"L":50,"C":100,"D":500,"M":1000}
        if len(s)==1:
            return nums[s]
        skip = False
        total = 0
        specials = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        for i,c in enumerate(s):
            if skip:
                skip=False
                continue
            if i+1<len(s):
                pair = c+s[i+1]
                if pair in specials.keys():
                    print("pair %s" % pair)
                    total+=specials[pair]
                    skip=True
                    continue
            total+=nums[c]
        print(total)
        return total
        
s = Solution()
if 1:
    assert s.romanToInt("V") == 5
    assert s.romanToInt("X") == 10
    assert s.romanToInt("II") == 2
    assert s.romanToInt("III") == 3
    assert s.romanToInt("XII") == 12
    assert s.romanToInt("XXVII") == 27
    assert s.romanToInt("IV") == 4
    assert s.romanToInt("VI") == 6
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994
assert s.romanToInt("MCDLXXVI") == 1476

print("OK")
