class Solution:
    def maximum(self, a: int, b: int) -> int:
        k = (a - b)>>63
        return (1+k)*a-k*b

print(Solution().maximum(-1,2))
