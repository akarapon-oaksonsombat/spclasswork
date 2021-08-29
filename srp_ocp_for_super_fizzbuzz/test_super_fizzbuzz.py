import unittest
from super_fizzbuzz import super_fizzbuzz


class TestSuperFizzBuzz(unittest.TestCase):
    def test_integer(self):
        for test_number in range(0, 10000, 1):
            expected_result = ""
            if test_number % 3 == 0:
                expected_result += "Fizz"
            if test_number % 9 == 0:
                expected_result += "Fizz"
            if test_number % 5 == 0:
                expected_result += "Buzz"
            if test_number % 25 == 0:
                expected_result += "Buzz"
            if expected_result == "":
                expected_result = "NoFizzBuzz"
            self.assertEqual(super_fizzbuzz(test_number), expected_result)

    def test_negative(self):
        for test_number in range(0, -10000, -1):
            self.assertEqual(super_fizzbuzz(test_number), "InputOnlyPositiveInteger")


if __name__ == '__main__':
    unittest.main()
