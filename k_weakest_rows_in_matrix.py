# Problem 1337


class Solution:
    def k_weakest_rows(mat: list[list[int]], k: int) -> list[int]:
        new_list = []
        result = []
        for i in range(len(mat)):
            new_list.append((i, sum(mat[i])))
        new_list.sort(key=lambda a: a[1])

        for i in range(k):
            result.append(new_list[i][0])

        return result


if __name__ == "__main__":
    result = Solution.k_weakest_rows(
        [
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 0, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1],
        ],
        3,
    )
    print(result)  # output: [2,0,3]
