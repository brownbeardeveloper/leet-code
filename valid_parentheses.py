# Problem 20


class Solution:
    def is_valid(s: str) -> bool:
        while True:
            if "()" in s:
                s = s.replace("()", "")
            elif "[]" in s:
                s = s.replace("[]", "")
            elif "{}" in s:
                s = s.replace("{}", "")
            else:
                break

        return len(s) == 0


if __name__ == "__main__":
    result = Solution.is_valid("([)]")
    print(result)  # output: False
