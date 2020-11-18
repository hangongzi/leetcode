import numpy as np

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = np.zeros((len(word1)+1, len(word2)+1), dtype=np.int)
        dp[0] = np.arange(len(word2)+1)
        dp[:, 0] = np.arange(len(word1)+1)
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                d1 = dp[i-1, j]+1
                d2 = dp[i, j-1] + 1
                d3 = dp[i-1, j-1] + (1 if word1[i-1]!=word2[j-1] else 0)
                dp[i, j] = np.min([d1, d2, d3])

        return int(dp[-1, -1])

print(Solution().minDistance("horse", "ros"))
