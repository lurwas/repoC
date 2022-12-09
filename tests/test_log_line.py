"""
Unit tests for LogLine class
"""
import unittest
import csv
from typing import TextIO
from mock import patch
from log_parser_richard.log_line import LogLine


class TestLogLine(unittest.TestCase):
    """
    Unit tests for LogLine class
    """
    def setUp(self) -> None:
        """
        Creates the line object used in the tests below
        :return:
        """
        self.file = 'mouse'
        self.line_number = '42'
        self.message = 'meaning of life'
        self.line = LogLine(file=self.file,
                            line_number=self.line_number,
                            message=self.message)

    def test_line(self):
        """
        Tests constructions of line object
        :return:
        """
        self.assertEqual(self.line.file, 'mouse')
        self.assertEqual(self.line.line_number, '42')
        self.assertEqual(self.line.message, 'meaning of life')

    @patch('csv.writer')
    def test_csv_write(self, mock_my_class):
        """
        Tests the writing of csv
        :param mock_my_class:
        :return:
        """
        # TODO: fix this test so that we can get the rows written and verify them.
        cvs_file = TextIO()
        csv_writer_mock = csv.writer(cvs_file, quoting=csv.QUOTE_NONNUMERIC)
        self.line.write_csv_row(csv_writer_mock)
        self.assertTrue(mock_my_class.called)


if __name__ == '__main__':
    unittest.main()
