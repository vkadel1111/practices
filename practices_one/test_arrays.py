from unittest import TestCase
from arrays import solution

class Test(TestCase):
    def test_solution(self):
        solution([[True,False,False],
                  [True,True,False],
                  [False,False,False]])
