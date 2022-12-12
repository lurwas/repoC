"""
Unit tests for the ParseLine class
"""
import unittest
from log_parser_richard import parse_line


class TestParseLine(unittest.TestCase):
    """
    Unit test for the ParseLine class
    """
    def setUp(self) -> None:
        self.line_parser = parse_line.ParseLine()

    def test_parse_line(self):
        """
        Test parse line
        :return:
        """
        cc_file_name = '/a/dir/file.cc'
        cc_line_number = '42'
        cc_message = " warning: A message"
        example_line_cc: str = f'{cc_file_name}:' \
                               f'{cc_line_number}: ' \
                               f'{cc_message}'
        logged_line_cc = self.line_parser.parse_line(example_line_cc)
        self.assertEqual(logged_line_cc.file, cc_file_name)
        self.assertEqual(logged_line_cc.line_number, cc_line_number)
        self.assertEqual(logged_line_cc.message, cc_message)

        any_file_name = '/b/dir/another.any'
        any_line_number = '24'
        any_message = ' any message'

        example_line_any: str = f'{any_file_name}:' \
                                f'{any_line_number}: ' \
                                f'{any_message}'
        logged_line_any = self.line_parser.parse_line(example_line_any)
        self.assertEqual(logged_line_any.file, any_file_name)
        self.assertEqual(logged_line_any.line_number, any_line_number)
        self.assertEqual(logged_line_any.message, any_message)

    def test_parse_lines_no_match(self):
        """
        Test parse lines with no match
        :return:
        """
        example_line_without_match = 'All youre base are belong to us!'
        logged_line = self.line_parser.parse_line(example_line_without_match)
        self.assertIsNone(logged_line)

    def test_parse_lines_no_file_match_group(self):
        """
        Test parse lines with no file match group
        :return:
        """
        example_line_without_file = '/no/file/just/directory'
        self.line_parser.pattern = r".+\w+"
        logged_line = self.line_parser.parse_line(example_line_without_file)
        self.assertIsNone(logged_line)

    def test_parse_lines_no_line_number(self):
        """
        Test parse lines with no line numbers group
        :return:
        """
        line_no_number = '/no/file/just/directory/fileButNoLine.cc'
        self.line_parser.pattern = r".+\w+"
        logged_line = self.line_parser.parse_line(line_no_number)
        self.assertIsNone(logged_line)

    def test_parse_lines_no_message(self):
        """
        Test parse lines with no message group
        :return:
        """
        example_line_without_message = '/a/dir/any.cc:42'
        self.line_parser.pattern = r".+\w+"
        logged_line = self.line_parser.parse_line(example_line_without_message)
        self.assertIsNone(logged_line)


if __name__ == '__main__':
    unittest.main()
