# Problem 58


class Solution:
    def length_of_last_word(s: str) -> int:
        try:
            s_list = s.strip().split(" ")
            return len(s_list[-1])
        except ValueError:
            return None


if __name__ == "__main__":
    result = Solution.length_of_last_word(" Winter is coming ")
    print(result)  # output: 6
