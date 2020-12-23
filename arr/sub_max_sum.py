from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 动态规划
        for i in range(1, len(nums)):
            nums[i] += max(nums[i-1], 0)
        return max(nums)
        # 暴力破解
        # ans = None
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         sum_n = sum(nums[i:j+1])
        #         if ans is None or ans<sum_n:
        #             ans = sum_n
        # return ans

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
