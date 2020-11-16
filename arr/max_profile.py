class Solution:
    def maxProfit(self, prices: list) -> int:
        # 动态规划
        dp = []
        for i in range(len(prices)):
            dp.append([0, 0])
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])

        return dp[len(prices)-1][0]
        # if not prices or len(prices) == 1:
        #     return 0
        # profit = 0
        # for i in range(1, len(prices)):
        #     if prices[i] > prices[i - 1]:
        #         profit += prices[i]-prices[i-1]
        #
        # return profit

print(Solution().maxProfit([7,1,5,3,6,4]))
