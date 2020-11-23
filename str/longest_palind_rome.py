import numpy as np

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 动态规划
        n = len(s)
        dp = np.zeros((n, n), dtype=np.int)
        ans = ""
        for l in range(n):
            for i in range(n):
                j = i+l
                if j>=len(s):
                    break
                if l == 0:
                    dp[i, i] = True
                elif l == 1:
                    dp[i, i+1] = s[i]==s[i+1]
                else:
                    dp[i, j] = dp[i+1, j-1] and (s[i]==s[j])

                if dp[i, j] and l+1>len(ans):
                    ans = s[i: j+1]
        return ans

print(Solution().longestPalindrome("bba"))
