from unittest import TestCase
from three_non_empty import solution

class Test(TestCase):
    def test_solution(self):
        assert solution("xzxzx") == 5
    def test_solution1(self):
        assert solution("xzy") == 1
    def test_solution2(self):
        assert solution("xxx") == 0
    def test_solution3(self):
        assert solution("xzxzxzxzxz") == 30
    def test_solution4(self):
        assert solution("xxxxxxxxxx") == 24
    def test_solution5(self):
        assert solution("xzxzxxzzxx") == 36
    def test_solution6(self):
        assert solution("gggggggggggggggggggggggggggggg") == 366
    def test_solution7(self):
        assert solution("gfgfgfgfgfgfgfgfgfgfgfgfgfgfgf") == 387