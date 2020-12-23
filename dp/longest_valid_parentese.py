import numpy

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_length = 0
        dp = numpy.zeros(len(s), dtype=numpy.int)
        for i in range(1, len(s)):
            if s[i]==')':
                if s[i-1]=='(':
                    dp[i] = 2+ (dp[i-2] if i>=2 else 0)
                elif i - dp[i-1]>0 and s[i-dp[i-1]-1]=='(':
                    dp[i] = dp[i-1] + 2 + (dp[i-dp[i-1]-2] if i-dp[i-1]-2>=0 else 0)
                max_length = max(dp[i], max_length)

        return max_length

print(Solution().longestValidParentheses("()"))
