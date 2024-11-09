# Problem 3248


class Solution:
    def final_position_of_snake(n: int, commands: list[str]) -> int:
        x, y = 0, 0

        for cmd in commands:
            if cmd == "RIGHT":
                x += 1
            elif cmd == "DOWN":
                y += 1
            elif cmd == "LEFT":
                x -= 1
            elif cmd == "UP":
                y -= 1

        return n * y + x


if __name__ == "__main__":
    result = Solution.final_position_of_snake(3, ["DOWN", "RIGHT", "UP"])
    print(result)  # output: 1
