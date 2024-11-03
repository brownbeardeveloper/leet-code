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
