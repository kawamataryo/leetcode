#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        purchase_price = 10**4 + 1
        current_profit = 0

        for i in range(1, len(prices)):
            yesterday_price = prices[i - 1]
            today_price = prices[i]

            if yesterday_price < purchase_price:
                purchase_price = yesterday_price

            tmp_profit = today_price - purchase_price
            if tmp_profit > current_profit:
                current_profit = tmp_profit

        return current_profit


# @lc code=end
