# Problem 121


class Solution:
    def max_profit(prices: list[int]) -> int:
        profit = 0
        buy = prices[0]

        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell

        return profit


if __name__ == "__main__":
    result = Solution.max_profit([7, 1, 5, 3, 6, 4])
    print(result)  # output: 5
