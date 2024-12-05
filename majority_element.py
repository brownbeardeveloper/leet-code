# Problem 169


class Solution:
    def majority_element(nums: list[int]) -> int:
        num_dict = {}

        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1

        print(num_dict)
        return max(num_dict, key=num_dict.get)


if __name__ == "__main__":
    nums_list = [0, 1, 2, 2, 3, 0, 4, 2]
    result = Solution.majority_element(nums_list)
    print(result)  # output: 2
