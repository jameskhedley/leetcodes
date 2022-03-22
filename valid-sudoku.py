"""
Runtime: 116 ms. Your runtime beats 68.24 % of python3 submissions.
"""
from typing import List
board0 = \
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board1 = \
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

#print(board)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check_series(row):
            nrow = [int(x) for x in row if x!="."]
            counts = {c: sum([x==c for x in nrow]) for c in set(nrow)}
            for cv in counts.values():
                if cv > 1: return False
            return True


        BOARD_SIZE = len(board)
        for row in board:
            if not check_series(row):
                return False
        for pos in range(len(board[0])):
            col = [row[pos] for row in board]
            if not check_series(col):
                return False

        for xcorner in range(0,BOARD_SIZE,3):
            for ycorner in range(0,BOARD_SIZE,3):
                offsets = [(xcorner, ycorner), (xcorner, ycorner+1), (xcorner, ycorner+2),
                        (xcorner+1, ycorner), (xcorner+1, ycorner+1), (xcorner+1, ycorner+2),
                        (xcorner+2, ycorner), (xcorner+2, ycorner+1), (xcorner+2, ycorner+2)]
                subgrid = []
                for off in offsets:
                    subgrid.append(board[off[0]][off[1]])
                if not check_series(subgrid):
                    return False

        return True

s = Solution()
assert s.isValidSudoku(board0) == True
assert s.isValidSudoku(board1) == False
print("All OK")