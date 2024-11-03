# Problem 412


class Solution:
    def fizz_buzz(n: int) -> list[str]:
        list = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                list.append("FizzBuzz")
            elif i % 3 == 0:
                list.append("Fizz")
            elif i % 5 == 0:
                list.append("Buzz")
            else:
                list.append(str(i))
        return list


if __name__ == "__main__":
    result = Solution.fizz_buzz(15)
    print(result)
    # output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
