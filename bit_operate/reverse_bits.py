class Solution:
    def reverseBits(self, num: int) -> int:
        if ~num == 0: return 32
        pre = 0
        cur = 0
        ans = 0
        for _ in range(32):
            if num&1:
                cur += 1
            else:
                pre = cur
                cur = 0
            ans = max(ans, pre+cur+1)
            num >>= 1
        return ans

print(Solution().reverseBits(0))
