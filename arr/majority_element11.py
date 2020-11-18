from collections import Counter
import math


class Solution:
    def majorityElement(self, nums: list) -> list:
        # 摩尔投票法
        if not nums:
            return []
        cand1 = nums[0]
        count1 = 0
        cand2 = nums[0]
        count2 = 0
        for i in nums:
            if cand1 == i:
                count1 += 1
                continue
            if cand2 == i:
                count2 += 1
                continue
            if count1 == 0:
                cand1 = i
                count1 += 1
                continue
            if count2 == 0:
                cand2 = i
                count2 += 1
                continue
            count1 -= 1
            count2 -= 1

        count1 = 0
        count2 = 0
        for i in nums:
            if cand1 == i:
                count1 += 1
            elif cand2 == i:
                count2 += 1

        res = []
        if count1>len(nums)/3:
            res.append(cand1)
        if count2>len(nums)/3:
            res.append(cand2)

        return res


print(Solution().majorityElement([3,2,3]))
