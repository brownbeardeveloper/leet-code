# Problem #231

import math


class Solution:
    def power_of_two(n: int) -> bool:
        return n > 0 and math.log2(n).is_integer()


if __name__ == "__main__":
    result = Solution.power_of_two(63)
    print(result)  # output: False
