class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            print(n)
            digits = [int(x) for x in list(str(n))]
            sum_digits = sum([x**2 for x in digits])
            if sum_digits==1: 
                return True
            elif sum_digits in seen:
                return False
            else:
                seen.add(int(sum_digits))
                n = int(sum_digits)


s = Solution()
assert s.isHappy(19) == True
assert s.isHappy(2) == False
print("All OK")
