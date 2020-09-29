"""Say you have an array prices for which the ith 
element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions 
at the same time (i.e., you must sell the stock before you buy again)."""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        stock = 0
        buy = False
        
        for i in range(len(prices)):
            
            current_price = prices[i]
            next_day_price = prices [i+1] if i != len(prices) -1 else 0
            
            
            
            if not buy and current_price < next_day_price:
                stock = current_price
                buy = True
            
            if buy and stock < current_price and current_price > next_day_price:
                profit += current_price - stock
                stock = 0 
                buy = False
        
        return profit