class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # print(f"input is {prices}\n")
        max_profit = 0
        i = 0
        for i in range(len(prices)-1):
            j = i+1
            while j <= len(prices) - 1:
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)
                # print(f"i: {i}, prices[i]: {prices[i]} | j: {j}, prices[j]: {prices[j]} | profit: {profit} | max_profit: {max_profit}")
                j += 1


        return max_profit