# Problem #9


class Solution:
    def is_palindrome(self, x: int) -> bool:
        return self.reverse_number(x) == str(x)

    def reverse_number(self, x: int) -> str:
        y = str(x)
        return y[::-1]


if __name__ == "__main__":
    solution = Solution()
    result = solution.is_palindrome(123454321)
    print(result)  # output: True
