from typing import List
#import copy

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[1]]
        if numRows == 1:
            return arr
        for i in range(numRows-1):
            last_row = arr[i]
            if last_row == [1]:
                new_row = [1,1]
            else:
                new_row = [1,1]
                for i, num in enumerate(last_row[:-1]):
                    sum0 = sum([last_row[i], last_row[i+1]])
                    new_row.insert(i+1,sum0)
            arr.append(new_row)
        print(arr)
        return arr
        
        
s = Solution()
if 1:
    assert s.generate(1) == [[1]]
    assert s.generate(2) == [[1],[1,1]]
    assert s.generate(3) == [[1],[1,1],[1,2,1]]
    assert s.generate(4) == [[1],[1,1],[1,2,1],[1,3,3,1]]
assert s.generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

print("All good")
