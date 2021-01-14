class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        return bin((A&0xFFFFFFFF)^(B&0xFFFFFFFF)).count('1')
print(Solution().convertInteger(826966453,-729934991))
