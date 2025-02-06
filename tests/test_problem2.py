# tests/test_problem1.py
import unittest
from problems.problem_2 import problem_2  

class TestProblem2(unittest.TestCase):  
    def test_solution_small_limit(self):
        problem = problem_2(10)  
        self.assertEqual(problem.solve(), 10)  

    def test_solution_large_limit(self):
        problem = problem_2(1000)  
        self.assertEqual(problem.solve(), 798)  

if __name__ == '__main__':
    unittest.main()

