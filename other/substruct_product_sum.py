from functools import reduce
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        while n:
            product *= n%10
            sum += n%10
            n = n//10
        return product-sum
        # return reduce(lambda product, x:product*x, nums, 1)-reduce(lambda sum, x: sum+x, nums, 0)

print(Solution().subtractProductAndSum(4421))