class Solution:
    def numberOfSteps (self, num: int) -> int:
        ret = 0
        while num:
            ret += 1
            if num % 2:
                num -= 1
            else:
                num /= 2
        return ret


print(Solution().numberOfSteps(123))
