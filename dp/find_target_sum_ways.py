from copy import copy

def findTargetSumWays(nums: list, S: int):
    n = len(nums)
    dp = [0]*2001
    dp[nums[0]+1000] = 1
    dp[-nums[0]+1000] += 1
    for i in range(n):
        next_ = [0]*2001
        for sum_ in range(-1000, 1001):
            if dp[sum_+1000]>0:
                next_[sum_+nums[i]+1000] += dp[sum_+1000]
                next_[sum_-nums[i]+1000] += dp[sum_+1000]
        dp = copy(next_)
    return 0 if S>1000 else dp[S+1000]

print(findTargetSumWays([1,1,1,1,1], 3))

