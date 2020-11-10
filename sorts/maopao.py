# 冒泡排序

class Solution:
    def bubbleSort(self, nums: list):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]>nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
                
        return nums

print(Solution().bubbleSort(nums=[2,3,1,4,6,5]))
