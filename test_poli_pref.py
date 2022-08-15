from unittest import TestCase
from poli_pref import solution

class Test(TestCase):
    def test_solution(self):
        assert solution("aaacodedoc") == ""
    def test_solution(self):
        assert solution("abbab") == "b"
    def test_solution(self):
        assert solution("aaabba") == "a"
    def test_solution(self):
        assert solution("aaaaaaab") == "b"
    def test_solution(self):
        assert solution("abbaabbaabba") == ""
    def test_solution(self):
        assert solution("a") == "a"