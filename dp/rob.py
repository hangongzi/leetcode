class Solution:
    def rob(self, nums: list) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        if len(nums) == 2:
            if nums[0]>nums[1]:
                return nums[0]
            else:
                return nums[1]
            
        size = len(nums)
        dp = [0]*size
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            # dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            if dp[i-1]>dp[i-2]+nums[i]:
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-2]+nums[i]
        return dp[-1]
        
        # now = 0 # dp[n]
        # pre = 0 # dp[n-1]
        # for i in range(len(nums)):
        #     now, pre = max(now, pre+nums[i]), now
        # return now

print(Solution().rob([1,2,3,1]))
