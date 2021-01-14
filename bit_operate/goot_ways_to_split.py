"""
给你一个字符串 s ，一个分割被称为 「好分割」 当它满足：
将 s 分割成 2 个字符串 p 和 q ，它们连接起来等于 s 且 p 和 q 中不同字符的数目相同。

请你返回 s 中好分割的数目。
"""

class Solution:
    def numSplits(self, s: str) -> int:
        n = len(s)
        left, right = [0]*(n+2), [0]*(n+2)

        rec_left = [False]*26
        rec_right = [False]*26

        for i in range(1, n+1):
            c = ord(s[i-1])-ord('a')
            if rec_left[c]:
                left[i] = left[i-1]
            else:
                rec_left[c] = True
                left[i] = left[i-1]+1
        
        for i in range(n, 0, -1):
            c = ord(s[i-1])-ord('a')
            if rec_right[c]:
                right[i] = right[i+1]
            else:
                right[i] = right[i+1]+1
                rec_right[c] = True
        ret = sum(1 for i in range(1, n) if left[i]==right[i+1])
        return ret

print(Solution().numSplits("abcd"))
