class Solution:
    def two_sum(nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == "__main__":
    result = Solution.two_sum([2, 7, 11, 15], 9)
    print(result)  # output: [0,1]
