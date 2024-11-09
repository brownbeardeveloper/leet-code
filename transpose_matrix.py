# Problem 867


import numpy as np


class Solution:
    def transpose(matrix: list[list[int]]) -> list[list[int]]:
        new_matrix = np.array(matrix)
        new_matrix = new_matrix.transpose()
        return new_matrix.tolist()


if __name__ == "__main__":
    result = Solution.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(result)  # output: [[1,4,7],[2,5,8],[3,6,9]]
