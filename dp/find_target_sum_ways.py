from copy import copy

def findTargetSumWays(nums: list, S: int):
    dp = {0:1} 
    for n in nums:
        prev = dp
        dp = {}
        
        for i in prev:
            dp[i + n] = dp[i + n] + prev[i] if (i + n) in dp else prev[i]
            dp[i - n] = dp[i - n] + prev[i] if (i - n) in dp else prev[i]
            
    return dp[S] if S in dp else 0

print(findTargetSumWays([1,1,1,1,1], 3))

