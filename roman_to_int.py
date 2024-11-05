# Problem # 13

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.


class Solution:
    def __init__(self):
        self.roman_dict = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }

    def roman_to_int(self, s: str) -> int:
        sum = 0
        i = 0

        while len(s) > i:
            if len(s) > i + 1 and s[i] + s[i + 1] in self.roman_dict:
                sum += self.roman_dict[s[i] + s[i + 1]]
                i += 2
            else:
                sum += self.roman_dict[s[i]]
                i += 1

        return sum


if __name__ == "__main__":
    solution = Solution()
    result = solution.roman_to_int("MCMXCIV")
    print(result)  # output: 1994
