class Solution(object):
    def maxProfit(self, prices):
        left, right, maxProfit = 0, 0, 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1

        return maxProfit
        
        