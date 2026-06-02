class Solution(object):
    def maxProfit(self, prices):
        if not len(prices): return 0
        dp = [[0,0] for _ in range(len(prices))]
        dp[0][1] = -prices[0]
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],-prices[i])
        return dp[-1][0]