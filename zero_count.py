class Solution:
    def moveZeros(self, nums:list):
        j = 0 # 永远记录0的位置
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j]=nums[i]
                if i!=j:
                    nums[i]=0
                j+=1


nums = [0, 1, 0, 3, 12]

Solution().moveZeros(nums)
print(nums)