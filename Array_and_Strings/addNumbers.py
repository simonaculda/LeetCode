import unittest


def add(a, b):
    return a + b


class TestAdd(unittest.TestCase):
    def test(self, sol):
        self.assertEqual(sol(2,2), 4)
