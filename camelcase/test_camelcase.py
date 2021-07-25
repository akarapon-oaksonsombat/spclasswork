import unittest
import camelcase


class TestStairCase(unittest.TestCase):
    def test_HelloWorld(self):
        self.assertEqual(camelcase.count_word('HelloWorld'), 2, 'Should be 2')

    def test_ILoveYou(self):
        self.assertEqual(camelcase.count_word('ILoveYou'), 3, 'Should be 3')


if __name__ == '__main__':
    unittest.main()
