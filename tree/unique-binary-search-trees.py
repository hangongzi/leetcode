class Solution(object):
    def numTrees(self, n):
        # 卡兰塔数
        C = 1
        for i in range(n):
            C = C*2*(2*i+1)//(i+2)

        return C
        # 动态规划
        # G = [0]*(n+1)
        # G[0], G[1] = 1, 1
        # for i in range(2, n+1):
        #     for j in range(1, i+1):
        #         G[i] += G[j-1]*G[i-j]
        # return G[n]
print(Solution().numTrees(3))
