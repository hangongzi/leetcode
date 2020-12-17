from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.s = []
        def backtrace(l, r):
            if len(self.s) == 2*n:
                ans.append(''.join(self.s))
                return
            if l>0:
                self.s.append('(')
                backtrace(l-1, r)
                self.s.pop()
            if l<r:
                self.s.append(')')
                backtrace(l, r-1)
                self.s.pop()
        backtrace(n, n)
        return ans


print(Solution().generateParenthesis(3))
