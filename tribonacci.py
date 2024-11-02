# Problem #1137


from functools import cache


class Solution:
    @cache
    def trib(self, n: int) -> int:
        if n == 1 or n == 0:
            return n
        elif n == 2:
            return 1
        return self.trib(n - 1) + self.trib(n - 2) + self.trib(n - 3)


if __name__ == "__main__":
    s = Solution()
    result = s.trib(5)
    print(result)  # output: 7
