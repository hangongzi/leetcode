from collections import Counter

class Solution:
    def majorityElement(self, nums: list):
        count = Counter(nums)
        return max(count, key=count.get)

print(Solution().majorityElement([2,2,1,1,1]))