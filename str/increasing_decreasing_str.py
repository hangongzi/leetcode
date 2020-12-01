class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        buckets = [0 for _ in range(26)]
        for c in s:
            buckets[ord(c)-97] += 1

        res = []
        while sum(buckets)>0:
            for i in range(26):
                if buckets[i]>0:
                    res.append(chr(i+97))
                    buckets[i] -= 1
            for i in range(25, -1, -1):
                if buckets[i]>0:
                    res.append(chr(i+97))
                    buckets[i] -= 1

        return ''.join(res)


print(Solution().sortString("aaaabbbbcccc"))
