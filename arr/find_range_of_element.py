class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        def searchBound(nums: list, target: int, left: bool)->int:
            l, r = 0, len(nums)
            while l<r:
                mid = (r+l)//2
                if nums[mid]>target or (left and target==nums[mid]):
                    r = mid
                else:
                    l = mid +1
            return l

        idx = searchBound(nums, target, True)
        if idx == len(nums) or nums[idx] != target:
            return [-1, -1]
        return [idx, searchBound(nums, target, False)-1]

    
print(Solution().searchRange([5,7,7,8,8,10], 8))
