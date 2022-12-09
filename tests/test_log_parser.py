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

    def test_open_file(self):
        """
        Test open file
        :return:
        """
        test_parser = log_parser.LogParser()
        test_parser.filename = 'agent42.txt'
        with patch('builtins.open', unittest.mock.mock_open()) as mock_open:
            test_parser.read_lines_from_file()
            mock_open.assert_called_once_with(test_parser.filename)

    @patch('os.path.isfile')
    def test_run(self, mock_isfile):
        """
        Test run
        :param mock_isfile: Mock for the os isfile call
        :return:
        """
        args = []
        test_parser = log_parser.LogParser()
        test_parser.parse_parameters(args)
        with patch('builtins.open', unittest.mock.mock_open()):
            mock_isfile.return_value = True
            test_parser.read_lines_from_file()
            self.assertTrue(test_parser.run(args))

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
        example_line_cc: str = "/accepts/lines/like/this/any_file.cc:42: warning: A meaning of life"
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
