# Problem #217


class Solution:
    def contains_duplicate(nums: list[int]) -> bool:
        return len(list(set(nums))) != len(nums)


if __name__ == "__main__":
    result = Solution.contains_duplicate([1, 2, 3, 4, 5, 6, 2])
    print(result)  # output: True
