class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        boxs = [{} for _ in range(9)]

        for row in range(9):
            for col in range(9):
                box_idx = (row-3)//3*3+col//3
                num = board[row][col]

                if num != ".":
                    rows[row][num] = rows[row].get(num, 0) + 1
                    cols[col][num] = cols[col].get(num, 0) + 1
                    boxs[box_idx][num] = boxs[box_idx].get(num, 0) + 1

                    if rows[row][num]>1 or cols[col][num]>1 or boxs[box_idx][num]>1:
                        return False
        return True

print(Solution().isValidSudoku(
    [["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]
))
