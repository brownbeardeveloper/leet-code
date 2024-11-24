# Problem 69


class Solution:
    def sqrt(x: int) -> int:
        right = x
        left = 0

        while left <= right:
            mid = (right + left) // 2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid

        return right


if __name__ == "__main__":
    result = Solution.sqrt(64)
    print(result)  # output: 8
