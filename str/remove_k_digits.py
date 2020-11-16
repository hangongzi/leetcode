class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remain = len(num)-k
        for i in range(len(num)):
            while k and stack and stack[-1]>num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])

        ret = ''.join(stack[:remain]).lstrip('0')
        return ret if ret else '0'


print(Solution().removeKdigits('1432219', 3))