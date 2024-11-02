# Problem #342

import math


class Solution:
    def power_of_base(n: int, base: int = 4) -> bool:
        return n > 0 and n == base ** round(math.log(n, base))


if __name__ == "__main__":
    result = Solution.power_of_base(1024)
    print(result)  # output: True
