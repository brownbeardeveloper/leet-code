# Problem 942


class Solution:
    def diStringMatch(s: str) -> list[int]:
        increasing = 0
        decreasing = len(s)
        new_list = []

        for i in range(len(s)):
            if s[i] == "I":
                new_list.append(increasing)
                increasing += 1

            elif s[i] == "D":
                new_list.append(decreasing)
                decreasing -= 1

        new_list.append(increasing)
        return new_list


if __name__ == "__main__":
    result = Solution.diStringMatch("IDID")
    print(result)  # output: [0, 4, 1, 3, 2]
