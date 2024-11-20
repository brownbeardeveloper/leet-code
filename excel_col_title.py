# Problem #168
import xlsxwriter


class Solution:
    def convert_to_title(columnNumber: int) -> str:
        return xlsxwriter.utility.xl_col_to_name(columnNumber - 1)


if __name__ == "__main__":
    result = Solution.convert_to_title(1337)
    print(result)  # output: AYK
