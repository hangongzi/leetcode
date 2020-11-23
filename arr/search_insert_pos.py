class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        ans = len(nums)
        l, r = 0, len(nums)-1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid]>=target:
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans


print(Solution().searchInsert([1,3,5,6], 7))