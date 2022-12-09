"""
Unit Tests for CsvWriter
"""
import unittest
from unittest.mock import patch
from log_parser_richard.csv_writer import CsvWriter
from log_parser_richard.log_line import LogLine


class TestCsvWriter(unittest.TestCase):
    """
    Tests for CsvWriter
    """

    def setUp(self) -> None:
        """
        Creates the csv_writer used in the tests
        :return:
        """
        self.csv_writer = CsvWriter()

    def test_write(self):
        """
        Tests write
        :return:
        """
        log_line = LogLine(file='file', line_number='42', message='Meaning of life')
        with patch('builtins.open', unittest.mock.mock_open()) as mock_open:
            self.csv_writer.write([log_line])
            mock_open.assert_called_once_with(self.csv_writer.filename,
                                              'w',
                                              encoding='UTF8',
                                              newline='')


if __name__ == '__main__':
    unittest.main()
