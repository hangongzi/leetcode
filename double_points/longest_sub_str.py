class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dp = {}
        front = 0
        ans = 0
        for i in range(len(s)):
            if s[i] in dp:
                front = dp[s[i]] + 1
            dp[s[i]] = i
            ans = max(ans, i-front+1)
        return ans

print(Solution().lengthOfLongestSubstring('dvdf'))
