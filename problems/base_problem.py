# problems/base_problem.py

from abc import ABC, abstractmethod

class BaseProblem(ABC):
    def __init__(self, limit=None):
        self.limit = limit

    @abstractmethod
    def solve(self):
        """Methode, die in jeder Unterklasse implementiert werden muss."""
        pass

    def run(self):
        """Optional: Führt die Lösung aus und gibt das Ergebnis aus."""
        result = self.solve()
        print(f"Lösung: {result}")
        return result
