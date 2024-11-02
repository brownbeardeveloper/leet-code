# Problem #231

import math


class Solution:
    def power_of_three(n: int) -> bool:
        return n > 0 and n == 3 ** round(math.log(n, 3))


if __name__ == "__main__":
    result = Solution.power_of_three(243)
    print(result)  # output: True
