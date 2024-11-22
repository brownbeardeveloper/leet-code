# Problem 999


class Solution:
    def num_rook_captures(self, board: list[list[str]]) -> int:
        r_position = self.find_r(board)
        row_list = []
        col_list = []

        # row
        for i in range(len(board[r_position[0]])):
            row_list.append(board[r_position[0]][i])

        # col
        for i in range(len(board)):
            col_list.append(board[i][r_position[1]])

        return self.captures_in_list(row_list) + self.captures_in_list(col_list)

    def find_r(self, board: list[list[str]]) -> int:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "R":
                    return (i, j)

    def captures_in_list(self, rook_list: list) -> int:
        find_p = False
        pass_r = False
        scores = 0

        for char in rook_list:
            if char == "p" and pass_r == False and find_p == False:
                find_p = True
            elif char == "B" and pass_r == True:
                break
            elif char == "B":  # and pass_r == False
                find_p = False
            elif char == "R" and find_p == True:
                scores += 1
                find_p = False
                pass_r = True
            elif char == "R":  # and find_p == False
                pass_r = True
            elif char == "p" and pass_r == True:
                scores += 1
                break

        return scores


if __name__ == "__main__":
    board = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", "R", ".", ".", ".", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
    ]
    solution = Solution()
    result = solution.num_rook_captures(board)
    print(result)  # output: 3
