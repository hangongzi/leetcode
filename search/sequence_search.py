class Solution:
    def sequenceSearch(self, nums: list, target: int)->int:
        for i in nums:
            if i == target: return nums.index(i)

        return -1

print(Solution().sequenceSearch([3,12,5,1,6], 12))
