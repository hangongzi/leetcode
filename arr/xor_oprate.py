class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        if n==0:
            return start
        return self.xorOperation(n-1, start)^(start+n*2)

        # result = start
        # i = 1
        # while i<n:
        #     result = result ^ (start+i*2)
        #     i+=1
        # return result

ret = Solution().xorOperation(5, 0)
print(ret)
# print(2^4)