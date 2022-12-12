"""
Unit tests for LogParser class
"""
import unittest
from unittest.mock import patch
from log_parser_richard import log_parser


class TestLogParser(unittest.TestCase):
    """
    Unit tests for LogParser class
    """
    def test_parse_parameters(self):
        """
        Test parse parameters
        :return:
        """
        expected_filename = 'unit_test.txt'
        args = ['--filename', expected_filename]
        test_parser = log_parser.LogParser()
        test_parser.parse_parameters(args)
        self.assertEqual(test_parser.filename, expected_filename)

    def test_parse_parameters_empty(self):
        """
        Test parse parameters when args are empty
        :return:
        """
        args = []
        test_parser = log_parser.LogParser()
        test_parser.parse_parameters(args)
        self.assertEqual(test_parser.filename, test_parser.default_file_name)

    @patch('builtins.open')
    def test_open_file(self, mock_file_open):
        """
        Test open file
        :return:
        """
        file_data = ['/a/file.cc:42: Warning: "mice"\n',
                     '/b/file.h:24: Warning: "dolphins"\n']
        mock_file_open.return_value.__enter__.return_value = file_data
        test_parser = log_parser.LogParser()
        test_parser.filename = 'agent42.txt'
        lines = test_parser.read_lines_from_file()
        self.assertEqual(file_data, lines)
        mock_file_open.assert_called_once_with(
            test_parser.filename,
            encoding='UTF8')

    @patch('builtins.open')
    @patch('os.path.isfile')
    def test_run(self, mock_isfile, mock_file_open):
        """
        Test run
        :param mock_isfile: Mock for the isfile call
        :param mock_file_open: Mock for the open call
        :return:
        """
        # with patch('builtins.open', unittest.mock.mock_open()):
        mock_isfile.return_value = True
        file_data = ['/a/file.cc:42: Warning: "mice"\n',
                     '/b/file.h:24: Warning: "dolphins"\n']
        mock_file_open.return_value.__iter__.return_value = file_data
        args = []
        test_parser = log_parser.LogParser()
        test_parser.parse_parameters(args)
        self.assertTrue(test_parser.run(args))
        self.assertTrue(mock_file_open.called)
        self.assertEqual((test_parser.csv_file.filename, 'w'),
                         mock_file_open.call_args[0])

    @patch('os.path.isfile')
    def test_run_no_file(self, mock_isfile):
        """
        Test run but no file exists
        :param mock_isfile:  Mock for the os isfile call
        :return:
        """
        args = []
        test_parser = log_parser.LogParser()
        test_parser.parse_parameters(args)
        with patch('builtins.open', unittest.mock.mock_open()):
            mock_isfile.return_value = False
            test_parser.read_lines_from_file()
            self.assertFalse(test_parser.run(args))

    def test_parse_lines(self):
        """
        Test parse lines
        :return:
        """
        test_parser = log_parser.LogParser()
        example_line_cc: str = \
            "/a/dir/any_file.cc:42: warning: A meaning of life"
        lines = [example_line_cc]
        self.assertIsNotNone(test_parser.parse_lines(lines))

    def test_parse_lines_no_log_lines_found(self):
        """
        Test parse lines no lines found
        :return:
        """
        test_parser = log_parser.LogParser()
        lines = ['Example line', 'Example second line']
        self.assertListEqual(test_parser.parse_lines(lines), [])


if __name__ == '__main__':
    unittest.main()
