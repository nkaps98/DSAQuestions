"""
Given an array prices[] of length n, representing the prices of the stocks on different days. The task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. If it is not possible to make a profit then return 0.

Note: Stock must be bought before being sold.

Examples:

Input: prices[] = [7, 10, 1, 3, 6, 9, 2]
Output: 8
Explanation: You can buy the stock on day 2 at price = 1 and sell it on day 5 at price = 9. Hence, the profit is 8.
"""


# Approach: One pass solution
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def maximumProfit(self, prices):
        # code here
        buy = -1
        max_profit = 0
        profit = 0
        prev_diff = 0
        sell = -1
        for i in range(len(prices)-1):
            # print(buy, max_profit)
            if prices[i+1] > prices[i] and buy == -1:
                buy = i
                
            elif prices[i+1] > prices[i] and buy != -1:
                if prices[buy] > prices[i]:
                    buy = i
            
            if buy!= -1 and prices[buy] < prices[i]:
                profit = prices[i] - prices[buy]
                
                if profit > max_profit:
                    max_profit = profit
                    sell = i
                    
        if buy!= -1 and prices[buy] < prices[i+1]:
            profit = prices[i+1] - prices[buy]
            
            if profit > max_profit:
                max_profit = profit
                sell = i
                
        return max_profit
                    
                
            