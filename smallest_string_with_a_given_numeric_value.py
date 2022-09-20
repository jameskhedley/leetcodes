"""
50 ms, faster than 90.97% of python3 submissions (pretty good!)
"""

import string

class Solution:
    def getSmallestString_old(self, n: int, k: int) -> str:
        '''
        1409 ms. Your runtime beats 22.66 % of python3 submissions (pretty bad)
        Faster way is to assume large numbers will be mostly zzzz at the end, 
        some a's at the front and one intermediate k value.
        '''
        chars = []
        digits = list(range(n))
        abc = list(string.ascii_lowercase)
        while digits:
            pos = digits.pop()
            min0 = min(k-pos, 26)
            c = abc[min0-1]
            chars.append(c)
            k-=min0
        final =  "".join(chars[::-1])
        return final
        
    def getSmallestString(self, n: int, k: int) -> str:
        abc = list(string.ascii_lowercase)
        how_many_zs = (k-n)//25
        zs = how_many_zs*"z"
        remain = (k-n) % 25
        if remain:
            nc=1
            c = abc[remain]
        else:
            nc=0
            c = ""
        how_many_as = (n-how_many_zs-nc)
        aas = how_many_as*"a"
        chars = aas+c+zs
        return chars

s = Solution()

assert s.getSmallestString(3,27) == "aay"

if 1:
    assert s.getSmallestString(5,130) == "zzzzz"
    assert s.getSmallestString(9,34) == "aaaaaaaaz"
    assert s.getSmallestString(5,73) == "aaszz"
print("All OK")