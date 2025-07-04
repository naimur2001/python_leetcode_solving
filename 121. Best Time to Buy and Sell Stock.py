# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        sell=0
        for i in range(1,len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            elif prices[i]-buy>sell:
                sell=prices[i]-buy
        return sell



s=Solution()
print(s.maxProfit([7,1,5,3,6,4]))

  # for i in range(1,len(prices)):  this method is time consuming (time complexity O(n^2))
  #           buy=min(buy,prices[i])
  #           sell=max(sell,prices[i]-buy)
  #       return sell     