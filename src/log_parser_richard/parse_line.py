"""
Parses a line from a doxygen warning log
"""
import re

from log_parser_richard.log_line import LogLine


class ParseLine:
    """
    Parses a line from a doxygen warning log
    Example lines:
    /a/dir/file.cc:42: Warning: 'A Message'
    """
    def __init__(self):
        self.pattern = r"(.+([.](\w+))):(\d+): (.*)"
        self.index_file_name = 1
        self.index_line_number = 4
        self.index_message = 5

    def parse_line(self, line):
        """
        Parses a line from a doxygen warning log
        :param line:
        :return: log line object with information about the line or None
        """
        match = re.search(self.pattern, line)
        if not match:
            return None
        try:
            file_name = match.group(self.index_file_name)
            line = match.group(self.index_line_number)
            message = match.group(self.index_message)
        except IndexError as index_error:
            print(f'Index error: {index_error}')
            # Returning None here since the IndexError shouldn't stop from parsing the next line
            return None

        my_log_line = LogLine(file=file_name, line_number=line, message=message)
        return my_log_line
