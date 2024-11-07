# Problem 682


class Solution:
    def cal_points(self, operations: list[str]) -> int:
        new_list = []
        i = 0

        while i < len(operations):
            print(new_list)
            if operations[i] == "+":
                new_list.append(new_list[-1] + new_list[-2])

            elif operations[i] == "D":
                new_list.append(new_list[-1] * 2)

            elif operations[i] == "C":
                del new_list[-1]
            else:
                new_list.append(int(operations[i]))
            i += 1
        return sum(new_list)


if __name__ == "__main__":
    solution = Solution()
    result = solution.cal_points(["5", "-2", "4", "C", "D", "9", "+", "+"])
    print(result)  # output: 27
