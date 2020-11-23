import re

class Solution:
    def myAtoi(self, s: str) -> int:
        # return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31-1), -2**31)
        print(*re.findall('^[\+\-]?\d+', s.lstrip()))

print(Solution().myAtoi("+-3.14"))
