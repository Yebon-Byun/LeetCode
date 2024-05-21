class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        prices : an array
        prices[i] : a given stock on the i th day
        
        Input: prices = [7,1,5,3,6,4]
        Output: 5
        """
        
        #1 Brute Force
#         max_profit = 0
#         for i in range(len(prices)-1):
#             for j in range(i + 1, len(prices)):
#                 profit = prices[j] - prices[i]
#                 if profit > max_profit:
#                     max_profit = profit
                    
#         return max_profit
    
        #2 One Pass
        min_price = float("inf")
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
            
        return max_profit
        
            
        
        