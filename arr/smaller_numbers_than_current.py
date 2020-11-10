from collections import Counter

class Solution:
    def smallerNumbersThanCurrent(self, nums: list) -> list:
        counts = Counter(nums)
        ret = []
        for i in nums:
            count = 0
            for k, v in counts.items():
                if k<i: count += v
            ret.append(count)
        return ret

print(Solution().smallerNumbersThanCurrent([6,5,4,8]))
