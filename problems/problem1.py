# problems/problem1.py
from problems.base_problem import BaseProblem

class problem_1(BaseProblem):
    def __init__(self, limit):
        super().__init__(limit)

    def is_multiple(self, number):
        return number % 3 == 0 or number % 5 == 0

    def solve(self):
        return sum(number for number in range(self.limit) if self.is_multiple(number))
