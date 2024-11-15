# Problem 303


class NumArray:
    def __init__(self, nums: list[int]):
        self.num_array = nums

    def sum_range(self, left: int, right: int) -> int:
        return sum(self.num_array[left : right + 1])
