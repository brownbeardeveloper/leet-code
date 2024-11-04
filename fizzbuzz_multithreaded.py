# Problem #1195

import threading
from typing import Callable


class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.counter = 1
        self.lock = threading.Lock()

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: "Callable[[], None]") -> None:
        while self.n >= self.counter:
            with self.lock:
                if self.counter % 3 == 0 and self.counter % 5 != 0:
                    printFizz()
                    self.counter += 1

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: "Callable[[], None]") -> None:
        while self.n >= self.counter:
            with self.lock:
                if self.counter % 5 == 0 and self.counter % 3 != 0:
                    printBuzz()
                    self.counter += 1

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: "Callable[[], None]") -> None:
        while self.n >= self.counter:
            with self.lock:
                if self.counter % 15 == 0:
                    printFizzBuzz()
                    self.counter += 1

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: "Callable[[int], None]") -> None:
        while self.n >= self.counter:
            with self.lock:
                if (
                    self.n >= self.counter
                    and self.counter % 3 != 0
                    and self.counter % 5 != 0
                    and self.counter % 15 != 0
                ):
                    printNumber(self.counter)
                    self.counter += 1


class LeetCodeList:
    def __init__(self):
        self.list = []

    def print_fizz_buzz(self):
        self.list.append("FizzBuzz")

    def print_buzz(self):
        self.list.append("Buzz")

    def print_fizz(self):
        self.list.append("Fizz")

    def print_number(self, n):
        self.list.append(n)

    def get_list(self):
        return self.list


if __name__ == "__main__":
    lcl = LeetCodeList()
    fb = FizzBuzz(15)

    thread_a = threading.Thread(target=fb.fizzbuzz, args=(lcl.print_fizz_buzz,))
    thread_b = threading.Thread(target=fb.buzz, args=(lcl.print_buzz,))
    thread_c = threading.Thread(target=fb.fizz, args=(lcl.print_fizz,))
    thread_d = threading.Thread(target=fb.number, args=(lcl.print_number,))

    thread_a.start()
    thread_b.start()
    thread_c.start()
    thread_d.start()
    thread_a.join()
    thread_b.join()
    thread_c.join()
    thread_d.join()

    print(lcl.get_list())
    # output: [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
