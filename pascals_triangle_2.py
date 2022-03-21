from typing import List
#import copy

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex+=1
        arr = [[1]]
        for i in range(rowIndex-1):
            last_row = arr[i]
            if last_row == [1]:
                new_row = [1,1]
            else:
                new_row = [1,1]
                for i, num in enumerate(last_row[:-1]):
                    sum0 = sum([last_row[i], last_row[i+1]])
                    new_row.insert(i+1,sum0)
            arr.append(new_row)
        ret = arr[-1]
        print(ret)
        return ret
        
        
s = Solution()
if 1:
    assert s.getRow(0) == [1]
    assert s.getRow(1) == [1,1]
    assert s.getRow(2) == [1,2,1]
    assert s.getRow(3) == [1,3,3,1]
assert s.getRow(4) == [1,4,6,4,1]

print("All good")
