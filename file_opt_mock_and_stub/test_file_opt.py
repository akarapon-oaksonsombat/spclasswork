from file_opt import rm_when_lower
import unittest
import mock


class OptTest(unittest.TestCase):
    # set up mock parameter.
    @mock.patch("file_opt.os.path")
    @mock.patch("file_opt.os")
    def test_remove_with_non_exit_path(self, mock_os, mock_os_path):
        # set up the mock.
        mock_os_path.isfile.return_value = False
        # call rm_when_lower with path which not exit.
        filename = mock.Mock("aaa")
        # test that the filename is lowercase.
        filename.isupper.return_value = False
        # call function to test.
        rm_when_lower(filename)
        # test that the os.remove function was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if present.")

    # set up mock parameter.
    @mock.patch("file_opt.os.path")
    @mock.patch("file_opt.os")
    def test_remove_with_exist_path(self, mock_os, mock_os_path):
        # make the file exist.
        mock_os_path.isfile.return_value = True
        # create MagicMock and call rm_when_lower function.
        filename = mock.MagicMock()
        # test that the filename is lowercase.
        filename.isupper.return_value = False
        # call function to test.
        rm_when_lower(filename)
        # test that the os.remove function was called with correctly path.
        mock_os.remove.assert_called_with(filename)

    # set up mock parameter.
    @mock.patch("file_opt.os.path")
    @mock.patch("file_opt.os")
    def test_decline_uppercase_path(self, mock_os, mock_os_path):
        # set up the mock.
        mock_os_path.isfile.return_value = False
        # call rm_when_lower with path which not exit.
        filename = mock.Mock("AAA")
        # test that the filename is uppercase.
        filename.isupper.return_value = True
        # call function to test.
        rm_when_lower(filename)
        # test that the os.remove function was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if present.")
