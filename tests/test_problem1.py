# tests/test_problem1.py
import unittest
from problems.problem1 import problem_1

class TestProblem1(unittest.TestCase):
    def test_solution_small_limit(self):
        problem = problem_1(10)
        self.assertEqual(problem.solve(), 23)  # 3 + 5 + 6 + 9 = 23

    def test_solution_large_limit(self):
        problem = problem_1(1000)
        self.assertEqual(problem.solve(), 233168)

if __name__ == '__main__':
    unittest.main()
