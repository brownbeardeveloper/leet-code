# Problem 1275


class Solution:
    def tic_tac_toe(self, moves: list[list[int]]) -> str:
        new_board = self.tic_tac_toe_board(moves)

        for i in range(len(new_board)):
            if "" != new_board[i][0] == new_board[i][1] == new_board[i][2]:
                return new_board[i][0]
            elif "" != new_board[0][i] == new_board[1][i] == new_board[2][i]:
                return new_board[0][i]

        if (
            "" != new_board[0][0] == new_board[1][1] == new_board[2][2]
            or "" != new_board[0][2] == new_board[1][1] == new_board[2][0]
        ):
            return new_board[1][1]

        return "Pending" if len(moves) < 9 else "Draw"

    def tic_tac_toe_board(self, moves: list[list[int]]) -> list[list[str]]:
        new_board = [["", "", ""], ["", "", ""], ["", "", ""]]

        for i in range(len(moves)):
            if i % 2 == 0:
                new_board[moves[i][0]][moves[i][1]] = "A"
            else:
                new_board[moves[i][0]][moves[i][1]] = "B"
            i += 1

        return new_board


if __name__ == "__main__":
    solution = Solution()
    result = solution.tic_tac_toe(
        [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
    )
    print(result)  # output: Draw
