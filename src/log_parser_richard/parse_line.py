"""
Parses a line from a doxygen warning log
"""
import re

from log_parser_richard.log_line import LogLine


class ParseLine:  # pylint: disable=too-few-public-methods
    """
    Parses a line from a doxygen warning log
    Example lines:
    /a/dir/file.cc:42: Warning: 'A Message'
    """

    def __init__(self):
        self.line_number_group = 'line_number'
        self.file_name_group = 'file_name'
        self.message_group = 'message'
        self.pattern = r"(?P<" + self.file_name_group + \
                       r">.+([.](\w+))):(?P<" + \
                       self.line_number_group + \
                       r">\d+): (?P<" + self.message_group + r">.*)"

    def parse_line(self, line_number):
        """
        Parses a line from a doxygen warning log
        :param line_number:
        :return: log line object with information about the line or None
        """
        match = re.search(self.pattern, line_number)
        if not match:
            return None
        try:
            file_name = match.group(self.file_name_group)
            line_number = match.group(self.line_number_group)
            message = match.group(self.message_group)
        except IndexError as index_error:
            print(f'Index error: {index_error}')
            # Returning None here since the IndexError shouldn't
            # stop from parsing the next line
            return None

        my_log_line = LogLine(file=file_name,
                              line_number=line_number,
                              message=message)
        return my_log_line
