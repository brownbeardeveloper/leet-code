# Problem 766


class Solution:
    def is_toeplitz_matrix(matrix: list[list[int]]) -> bool:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                if matrix[i][j] != matrix[i - 1][j - 1]:
                    return False
        return True


if __name__ == "__main__":
    result = Solution.is_toeplitz_matrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]])
    print(result)  # output: True
