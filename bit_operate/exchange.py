class Solution:
    def exchangeBits(self, num: int) -> int:
        odd = num&0x55555555
        event = num&0xaaaaaaaa
        return (odd<<1)|(event>>1)

print(Solution().exchangeBits(5))
