"""
Runtime: 698 ms. Your runtime beats 90.81 % of python3 submissions. (Good!)
"""

class Solution:
    def longestPalindrome0(self, s: str) -> str:
        if len(s) == 1: return s
        if self.isPalindrome(s):
            return s
        max = 0
        last_sub = s[0]
        for ll in range(2, len(s) + 1):
            subs = self.all_substrings(ll, s)
            for sub in subs:
                if self.isPalindrome(sub):
                    max = ll
                    last_sub = str(sub)
                    break
        return last_sub

    def longestPalindrome1(self, s: str) -> str:
        if len(s) == 1: return s
        if self.isPalindrome(s):
            return s
        for ll in range(len(s),1,-1):
            subs = self.all_substrings(ll, s)
            for sub in subs:
                if self.isPalindrome(sub):
                    return sub
        return s[0]

    def longestPalindrome(self, s):
        def inner(s,lp,rp):
            subs = s[0]
            while lp>=0 and rp<len(s):
                if s[lp]==s[rp]:
                    tmp = s[lp:rp+1]
                    if len(tmp) > len(subs):
                        subs = str(tmp)
                else:
                    break
                lp-=1
                rp+=1
            return subs
        if self.isPalindrome(s):
            return s
        subs = ""
        for i, _c in enumerate(s):
        #for i in [362]:
            lp=i
            rp=i

            found = inner(s,lp,rp)
            if len(found) > len(subs):
                subs = str(found)

            found = inner(s,lp,rp+1)
            if len(found) > len(subs):
                subs = str(found)

        return subs


    def isPalindrome(self, s0: str) -> bool:
        lp=0
        rp=len(s0)-1
        while lp<rp:
            if s0[lp] != s0[rp]:
                return False
            lp += 1
            rp -= 1
        return True

    def all_substrings(self, ll, s0):
        subs = []
        for i in range(len(s0)-(ll-1)):
            subs.append(s0[i:i+ll])
        return subs
    
s = Solution()

if 1:
    assert s.longestPalindrome('babad') == 'bab'
    assert s.longestPalindrome('cbbd') == 'bb'
    assert s.longestPalindrome('aca') == 'aca'
    assert s.longestPalindrome('babad') == 'bab'
    assert s.longestPalindrome('aca') == 'aca'
    assert s.longestPalindrome('cabac') == 'cabac'
    
    assert s.longestPalindrome('abbacabab') == 'bacab'
    assert s.longestPalindrome('ac') == 'a'

    t0 = "lphntrsqudccteewsdmpjmgmfnxegawjclzobpnxdrvxeygafiwyqsvsecictqkmiqvrdjajfngvlhdezdpqpzjjzbhoyggrbkuzeocrpzqishvfairdvvabopyubfisxbrgnlughbrzunitwowvnsqhdtnkotitgxwzjhbgltksorygpdberdgzgvogrvwluhixfbrfhliedjylxuspjpitwlhdkneonreqrueqphirmgxtqumllqropaefddplspkrtkbmuvwkyryworojlvwzdlacuoqzokrmcgmwkopsbqjjkaoqjqbrderwzmhbhfgwvrjakyfeqcbtvlcgbsxkngymxyievihiskdmmppmmdksihiveiyxmygnkxsbgclvtbcqefykajrvwgfhbhmzwredrbqjqoakjjqbspokwmgcmrkozqoucaldzwvljorowyrykwvumbktrkpslpddfeaporqllmuqtxgmrihpqeurqernoenkdhlwtipjpsuxlyjdeilhfrbfxihulwvrgovgzgdrebdpgyrosktlgbhjzwxgtitokntdhqsnvwowtinuzrbhgulngrbxsifbuypobavvdriafvhsiqzprcoezukbrggyohbzjjzpqpdzedhlvgnfjajdrvqimkqtcicesvsqywifagyexvrdxnpbozlcjwagexnfmgmjpmdsweetccduqsrtnhpl"
    #t0 = "dmmppmmd" #shorter version of above
    ans = s.longestPalindrome(t0)
    assert  ans == t0
    
    t1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    t11 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    assert s.longestPalindrome(t1) == t11
#print(s.longestPalindrome(t1))

print("All OK")



