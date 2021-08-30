# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Problem 121

class Solution:

    # minimum_so_far approach uses the idea of Kadane's algorithm
    def find_max_profit_with_minimum_so_far(self, prices):
        if len(prices) < 2:
            return 0
        max_profit = 0
        minimum_so_far = prices[0]
        for i in range(1, len(prices)):
            minimum_so_far = min(minimum_so_far, prices[i])
            max_profit = max(max_profit, prices[i] - minimum_so_far)
        return max_profit

    # two pointer approach
    def find_max_profit(self, prices):
        # l:left=buy  r:right=sell
        le, r = 0, 1
        max_profit = 0
        for r in range(len(prices)):
            if prices[le] < prices[r]:
                max_profit = max(max_profit, prices[r] - prices[le])
            else:
                le = r
        return max_profit


if __name__ == "__main__":
    input_array = [7, 2, 5, 3, 6, 1, 4]
    sol = Solution()
    # max_pro = sol.find_max_profit_with_minimum_so_far(input_array)
    max_pro = sol.find_max_profit(input_array)
    print(max_pro)

# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.

# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
