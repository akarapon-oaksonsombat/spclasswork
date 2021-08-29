import unittest
from super_fizzbuzz import super_fizzbuzz


class TestSuperFizzBuzz(unittest.TestCase):
    def test_integer(self):
        for number in range(1, 10000, 1):
            result = ""
            if number % 3 == 0:
                result += "Fizz"
            if number % 9 == 0:
                result += "Fizz"
            if number % 5 == 0:
                result += "Buzz"
            if number % 25 == 0:
                result += "Buzz"
            if result == "":
                result = "NoFizzBuzz"
            self.assertEqual(super_fizzbuzz(number), result)


if __name__ == '__main__':
    unittest.main()
