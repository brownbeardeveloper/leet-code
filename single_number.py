# Problem # 136


class Solution:
    def single_number(self, nums: list[int]) -> int:
        counter_dict = {}
        i = 0
        while len(nums) > i:
            counter_dict[nums[i]] = counter_dict.get(nums[i], 0) + 1
            i += 1

        for key, value in counter_dict.items():
            if value == 1:
                return key


if __name__ == "__main__":
    solution = Solution()
    result = solution.single_number([4, 1, 2, 1, 2, 4, 5, 4])
    print(result)  # output: 5
