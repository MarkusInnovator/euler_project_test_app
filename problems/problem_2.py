from problems.base_problem import BaseProblem

class problem_2(BaseProblem):
    def __init__(self, limit):
        super().__init__(limit)
        
    def solve(self):
        a, b = 1, 2  
        total = 0
        while b <= self.limit:
            if b % 2 == 0: 
                total += b
            a, b = b, a + b  
        return total
