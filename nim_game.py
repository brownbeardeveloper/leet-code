# Problem 292


class Solution:
    def can_win_nim(n: int) -> bool:
        return n % 4 > 0


if __name__ == "__main__":
    result = Solution.can_win_nim(23)
    print(result)  # output: True
