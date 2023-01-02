# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Right pointer starts from first index and left pointer starts from zeroth index 
# The method falls under sliding window and can be solved using 2 pointers system

def maxProfit (prices) -> int:
    left, right, maxProfit = 0, 1, 0

    while right < len(prices):
        # Check if the transaction of stock is profitable than last one
        if prices[left] < prices[right]:
            currentProfit = prices[right] - prices[left]
            maxProfit = max (currentProfit, maxProfit)
        else:
            # Increment the left pointer to right pointer when the price is not less than succeding stock
            left = right
        # Increment the right pointer irrespective of the condition
        right += 1

    return maxProfit

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    print (maxProfit (prices))
    # Input: prices = [7,1,5,3,6,4]
    # Output: 5
    # Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    # Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell
