class Solution:
    def removeZerosInArr(self, nums: list)->list:
        zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_index], nums[i] = nums[i], nums[zero_index]
                while nums[zero_index] != 0:
                    zero_index += 1 
        return nums

nums = [0, 1, 0, 2, 4, 6]
Solution().removeZerosInArr(nums)
