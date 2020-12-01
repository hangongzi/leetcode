class Solution:
    def canJump(self, nums: list) -> bool:
        k = 0
        for i in range(len(nums)):
            if i>k: return False
            else: k = max(k, i+nums[i])
        return True


print(Solution().canJump([3,2,1,0,4]))
