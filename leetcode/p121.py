class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        table = [-1] * n
        max_ = prices[n-1]
        table[n-1] = max_
        for i in range(n-2, -1, -1):
            max_ = max(max_, prices[i])
            table[i] = max_
        
        profit = 0
        for i in range(n-1):
            profit = max(profit, table[i+1] - prices[i])
            
        return profit
