import unittest


def add(a, b):
    return a + b


class TestAdd(unittest.TestCase):
    def test(self, sol):
        self.assertEqual(sol(3,3), 6)
