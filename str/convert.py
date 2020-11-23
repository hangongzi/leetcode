class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ['' for _ in range(numRows)]
        goingDonw = False
        curRow = 0

        for c in s:
            rows[curRow] = rows[curRow]+c
            if curRow==0 or curRow+1==numRows: goingDonw = not goingDonw
            curRow += 1 if goingDonw else -1

        return ''.join(rows)


print(Solution().convert("AB", 1))
