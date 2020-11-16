class Solution:
    def nextPermutation(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        print(nums)

        # flag = True
        # for i in range(1, len(nums)):
        #     if nums[i] > nums[i - 1]:
        #         flag = False
        #         break
        # if flag:
        #     nums.sort()
        #     return
        # for i in range(len(nums) - 1, -1, -1):
        #     if nums[i] > nums[i - 1]:
        #         tmp = []
        #         for j in range(i, len(nums)):
        #             if nums[j] > nums[i - 1]: tmp.append(nums[j])
        #         min_num = min(tmp)
        #         min_idx = nums[i:].index(min_num)+i
        #         nums[i - 1], nums[min_idx] = min_num, nums[i - 1]
        #         tmp = nums[i:]
        #         tmp.sort()
        #         nums[i:] = tmp
        #         break
        # print(nums)


Solution().nextPermutation([5, 4, 7, 5, 3, 2])
