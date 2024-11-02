from functools import cache


class Solution:
    def climbStairs(n: int) -> int:
        @cache
        def fib(i) -> int:
            if i == 1 or i == 0:
                return 1
            return fib(i - 1) + fib(i - 2)

        return fib(n)


if __name__ == "__main__":
    result = Solution.climbStairs(5)
    print(result)
