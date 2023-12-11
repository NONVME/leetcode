"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
"""
from typing import List


class Solution:
    """
    T-O(n)
    S-O(1)
    """
    def maxProfit(self, prices: List[int]) -> int:
        min_p = max_p = prices[0]
        delta = 0
        for index, p in enumerate(prices):
            if p < min_p:
                min_p = p
                max_p = p
            if p > max_p:
                max_p = p
            if (new_delta := max_p - min_p) > delta:
                delta = new_delta
        return delta


assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
assert Solution().maxProfit([4, 2, 4, 1]) == 2
