"""
Writes log lines to a csv file
"""
import csv
from collections.abc import Iterable

from log_parser_richard.log_line import LogLine


class CsvWriter:  # pylint: disable=too-few-public-methods
    """
    Tests for CsvWriter
    """
    def __init__(self):
        """
        Sets up the default csv file name to use and creates a header to use
        """
        self.filename = 'log_lines.csv'
        self.header = ['Line', 'File', 'Message']

    LogLines = Iterable[LogLine]

    def write(self, lines=LogLines):
        """
        Writes all the LogLines in the file
        :param lines: a list of LogLines
        :return:
        """
        with open(self.filename, 'w', encoding='UTF8', newline='') as csv_file:
            # Python 3 specific
            writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(self.header)
            for line in lines:
                line.write_csv_row(writer)
