from functools import reduce

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        
        # res = '1'
        # for _ in range(n-1):  # 控制循环次数
        #     i, tmp = 0, ''
        #     for j, c in enumerate(res):
        #         if c != res[i]:
        #             tmp += str(j-i) + res[i]
        #             i = j
        #     res = tmp + str(len(res) - i) + res[-1]
        # return res

print(Solution().countAndSay(6))
