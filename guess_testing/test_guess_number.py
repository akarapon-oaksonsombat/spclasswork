import guess_number
import unittest
import mock


class TestGuessInt(unittest.TestCase):
    @mock.patch("random.randint")
    def test_guess_int(self, mock_int):
        guess_number.guess_int(1, 10)
        mock_int.assert_called_once_with(1, 10)

    @mock.patch("random.randint")
    def test_guess_int_start_with_float(self, mock_int):
        guess_number.guess_int(1.2, 10)
        mock_int.assert_called_once_with(1, 10)

    @mock.patch("random.randint")
    def test_guess_int_stop_with_float(self, mock_int):
        guess_number.guess_int(1, 10.2)
        mock_int.assert_called_once_with(1, 10)

    @mock.patch("random.randint")
    def test_guess_int_call_with_float(self, mock_int):
        guess_number.guess_int(1.2, 10.2)
        mock_int.assert_called_once_with(1, 10)


class TestGuessFloat(unittest.TestCase):
    @mock.patch("random.uniform")
    def test_guess_float(self, mock_float):
        guess_number.guess_float(1.2, 10.2)
        mock_float.assert_called_once_with(1.2, 10.2)

    @mock.patch("random.uniform")
    def test_guess_start_with_int(self, mock_float):
        guess_number.guess_float(1, 10.2)
        mock_float.assert_called_once_with(1, 10.2)

    @mock.patch("random.uniform")
    def test_guess_stop_with_int(self, mock_float):
        guess_number.guess_float(1.2, 10)
        mock_float.assert_called_once_with(1.2, 10)

    @mock.patch("random.uniform")
    def test_guess_called_with_int(self, mock_float):
        guess_number.guess_float(1, 10)
        mock_float.assert_called_once_with(1, 10)


if __name__ == '__main__':
    unittest.main()
