class Solution:
    def runningSum(self, nums: list) -> list:
        for i in range(1, len(nums)):
            nums[i-1] += nums[i]
        return nums

nums = []
Solution().runningSum(nums)
