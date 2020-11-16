class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        num_index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[num_index]:
                num_index += 1
                nums[num_index] = nums[i]

        return num_index+1

nums = [0,0,1,1,1,2,2,3,3,4]

Solution().removeDuplicates(nums)
