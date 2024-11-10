# Problem 704


class Solution:
    def search(nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1


if __name__ == "__main__":
    result = Solution.search(nums=[-1, 0, 3, 5, 9, 12], target=2)
    print(result)  # output: -1
