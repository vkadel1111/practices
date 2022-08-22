from unittest import TestCase
from cross import  solution

class Test(TestCase):
    def test_solution(self):
        assert solution([[1,1,1,1],[2,1,0,1],[3,1,0,1]]) == 2
    def test_solution(self):
        assert solution([[0,0,0,0],[0,0,0,0],[0,0,0,0]]) == 3*4
    def test_solution(self):
        assert solution([[0],[0],[0]]) == 0
    def test_solution(self):
        assert solution([[4,4,0,4]]) == 1
    def test_solution(self):
        assert solution([[4,4,4,4]]) == 4

