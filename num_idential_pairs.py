class Solution:
    def numIdenticalPairs(self, nums: list) -> int:
        result = 0
        nums_l = [0]*100
        for i in nums:
            nums_l[i] += 1


        for v in filter(lambda x: x, nums_l):
            result += v*(v-1)//2
        return result
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]==nums[j]:
        #             result += 1
        # return result


Solution().numIdenticalPairs([1,1,1,1])