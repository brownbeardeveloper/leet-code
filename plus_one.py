# Problem 66


class Solution:
    def plus_one(digits: list[int]) -> list[int]:
        last_digit_index = len(digits) - 1
        digits[last_digit_index] += 1

        if digits[last_digit_index] == 10:
            for i in range(last_digit_index, -1, -1):
                if digits[i] == 10:
                    digits[i] = 0
                    if i == 0:
                        digits.insert(0, 1)
                    else:
                        digits[i - 1] += 1
                else:
                    break

        return digits


if __name__ == "__main__":
    result = Solution.plus_one([8, 9, 9, 9])
    print(result)  # output: [9,0,0,0]
