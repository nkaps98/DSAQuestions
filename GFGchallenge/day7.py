from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        buy = -1
        sell = -1
        
        profit = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                buy = i
                break
        
        for i in range(buy, len(prices)-1):
            if prices[i+1] > prices[i] and buy == -1:
                buy = i
                
            if prices[i+1] < prices[i] and buy != -1 and sell == -1:
                profit += prices[i] - prices[buy]
                buy = -1
                
        if buy != -1:
            profit += prices[i+1] - prices[buy]
        
        
        return profit
            