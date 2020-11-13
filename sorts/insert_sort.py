class Solution:
    def insertSort(self, nums: list):
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while key < nums[j] and j >= 0:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        return nums


print(Solution().insertSort([2, 3, 1, 5, 4, 6]))
