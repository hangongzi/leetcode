class Solution:
    def findLengthOfLCIS(self, nums: list) -> int:
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]: anchor = i
            ans = max(ans, i - anchor + 1)
        return ans

        # if not nums:
        #     return 0
        # count = 0
        # i = 0
        # ret = []
        # while i<len(nums):
        #     while i<len(nums)-1 and nums[i]<nums[i+1]:
        #         count += 1
        #         i += 1
        #     ret.append(count+1)
        #     i+=1
        #     count = 0
        # return max(ret)


print(Solution().findLengthOfLCIS([1,3,5,4,7, 8, 9, 10]))
