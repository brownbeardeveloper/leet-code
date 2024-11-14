# Problem #283


class Solution:
    def move_zeroes(nums: list[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                # swap elements without using a temporary variable
                nums[right], nums[left] = nums[left], nums[right]
                left += 1


if __name__ == "__main__":
    list = [0, 0, 1]
    result = Solution.move_zeroes(list)
    print(list)  # output: [1,0,0]
