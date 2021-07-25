import unittest
from staircase import staircase


class TestStairCase(unittest.TestCase):
    def test_staircase(self):
        self.assertEqual(staircase.staircase_row(10, 1), test_row(10, 1))

    def test_staircase(self):
        self.assertEqual(staircase.staircase_row(20, 1), test_row(20, 1))


def test_row(number, row):
    return f'{" " * (number - row)}' + f'{"#" * row}'


if __name__ == '__main__':
    unittest.main()
