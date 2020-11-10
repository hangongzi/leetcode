class Solution:
    def createTargetArray(self, nums: list, index: list) -> list:
        ret = []
        for i in range(len(nums)):
            ret.append(0)
            ret_idx = len(ret)-1
            while ret_idx > index[i]:
                ret[ret_idx] = ret[ret_idx-1]
                ret_idx -= 1
            ret[ret_idx] = nums[i]
        return ret

print(Solution().createTargetArray([1,2,3,4,0], [0,1,2,3,0]))