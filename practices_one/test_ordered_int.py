from unittest import TestCase
from ordered_int import solution


class Test(TestCase):
    def test_solution(self):
        assert solution([1, 3, 2, 1]) == False

    # [2,-1,1]
    def test_solution_2(self):
        assert solution([1, 3, 2]) == True

    # [2,1]
    def test_solution_3(self):
        assert solution([1, 2, 1, 2]) == False

    # [1,2,3,4,1,2,3,4] = [1,1,1,-1,1,1,1]
    # [1,-1,1]
    # [10,20,30,40,15,25,26,27] = [10,10,10,-25,1,1]
    def test_solution_4(self):
        assert solution([3, 6, 5, 8, 10, 20, 15]) == False

    # [3,-1,3,2,10,-5]
    def test_solution_5(self):
        assert solution([1, 1, 2, 3, 4, 4]) == False

    # [0,1,1,1,0]
    def test_solution_6(self):
        assert solution([1, 4, 10, 4, 2]) == False

    # [3,6,-6,-2]
    def test_solution_7(self):
        assert solution([10, 1, 2, 3, 4, 5]) == True

    # [-9,1,1,1]
    def test_solution_8(self):
        assert solution([1, 1, 1, 2, 3]) == False

    # [0,0,0,1,1]
    def test_solution_9(self):
        assert solution([0, -2, 5, 6]) == True
    # [-2,7,1]
    def test_solution_10(self):
        assert solution([3, 5, 67, 98, 3]) == True
    # [-2,7,1]
    def test_solution_11(self):
        assert solution([1, 4, 10, 4, 3]) == False
    # [-2,7,1]