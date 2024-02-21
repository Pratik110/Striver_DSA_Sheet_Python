class Solution(object):
    def maxProfit(self, prices):
        min_Price = prices[0]
        max_profit = 0
        n = len(prices)
        for i in range(n):
            currentDayPrice = prices[i]
            profit = currentDayPrice - min_Price
            max_profit = max(profit,max_profit)
            min_Price = min(min_Price,currentDayPrice)
        return max_profit

        

prices = [7,1,5,3,6,4]
s = Solution()
print(s.maxProfit(prices))