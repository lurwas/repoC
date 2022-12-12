"""
Holds a log line from a doxygen warning log
"""


class LogLine:  # pylint: disable=too-few-public-methods
    """
    Holds information about a log line from a doxygen warning log
    """

    def __init__(self, file, line_number, message):
        self.file = file
        self.line_number = line_number
        self.message = message

    def write_csv_row(self, writer):
        """
        Write the LogLine to a cvs row
        :param writer: a cvs writer object with a writerow method
        :return:
        """
        writer.writerow([self.line_number, self.file, self.message])
