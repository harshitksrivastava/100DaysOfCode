# recursive is more time and space taking approach but provides with an answer with O(N) time complexity
def recursive_func(i, elem, arr):
    if i >= len(arr):
        return 0
    max_profit = recursive_func(i + 1, arr[i], arr)
    maximum = max(arr[i:])
    current_profit = (elem - maximum) * -1
    if current_profit > max_profit:
        max_profit = current_profit
    return max_profit


# This is also an O(N) time complexity approach but takes a lot less time and space as compared to recursive approach
def maximum_profit(arr, n):
    min_price = arr[0]
    max_cost = 0
    for i in range(n):
        min_price = min(min_price, arr[i])
        cost = arr[i] - min_price
        max_cost = max(max_cost, cost)
    return max_cost


# Dynamic Programming approach
def dynamic_max_profit(prices):
    if len(prices) < 2:
        return 0
    dp = [0] * len(prices)
    dp[1] = prices[1] - prices[0]
    max_profit = max(dp[1], 0)
    for i in range(2, len(prices)):
        dp[i] = max(dp[i - 1] + (prices[i] - prices[i - 1]), prices[i] - prices[i - 1])
        max_profit = max(max_profit, dp[i])
    return max_profit


if __name__ == "__main__":
    maxi = 0
    input_array = [7, 2, 5, 3, 6, 1, 4]
    if len(input_array) == 0:
        max_pro = 0
    else:
        # max_pro = recursive_func(1, input_array[0], input_array)
        # max_pro = maximum_profit(input_array, len(input_array))
        max_pro = dynamic_max_profit(input_array)
    print(max_pro)
