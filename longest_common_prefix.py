# Problem #14


class Solution:
    def longest_common_prefix(strs: list[str]) -> str:
        base = strs[0]
        for i in range(len(base)):  # row
            for j in range(1, len(strs)):  # col
                if i >= len(strs[j]) or strs[j][i] != base[i]:
                    return base[:i]
        return base


if __name__ == "__main__":
    result = Solution.longest_common_prefix(["flower", "flow", "flight"])
    print(result)  # output: fl
