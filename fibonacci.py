# Problem #509


from functools import cache


class Solution:
    @cache
    def fib(self, n: int) -> int:
        if n == 1 or n == 0:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


if __name__ == "__main__":
    s = Solution()
    result = s.fib(4)
    print(result)  # output: 3
