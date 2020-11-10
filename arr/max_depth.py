from collections import deque

class Solution:
    def maxDepth(self, s: str) -> int:
        ret = 0
        dequeue = []
        for c in s:
            if c == '(':
                dequeue.append(c)
                ret = max(ret, len(dequeue))
            elif c == ')':
                dequeue.pop()

        return ret

print(Solution().maxDepth("1+(2*3)/(2-1)"))
