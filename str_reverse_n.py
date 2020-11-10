class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        if not s or n>=len(s):
            return s
        return s[n:]+s[:n]

ret = Solution().reverseLeftWords("abcdefg", 2)
print(ret)