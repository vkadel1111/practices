from unittest import TestCase
from deposit import solution

class Test(TestCase):
    def test_solution(self):
        assert solution(100, 20, 170) == 3
    def test_solution2(self):
        assert solution(20, 20, 50) == 6
