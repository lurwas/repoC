"""
Simple doxygen warning log parser
"""
import argparse
import os.path

from log_parser_richard.csv_writer import CsvWriter
from log_parser_richard.parse_line import ParseLine


class LogParser:
    """
    Simple doxygen warning log parser
    """
    def __init__(self):
        self.default_file_name = 'doxygen_warning.log'
        self.filename = None
        self.line_parser = ParseLine()
        self.parsed_lines = None
        self.csv_file = CsvWriter()

    def parse_parameters(self, args):
        """
        Parse the needed parameters
        :return:
        """
        application_description = 'Simple doxygen warning log parser'
        parser = argparse.ArgumentParser(prog='log_parser',
                                         description=application_description,
                                         epilog='have a nice day')
        parser.add_argument('-f', '--filename', default=self.default_file_name)
        args = parser.parse_args(args)
        self.filename = args.filename

        print(f'File to process: {self.filename}')

    def read_lines_from_file(self):
        """
        Opens a file and read lines from it
        :return: a list of lines found in the file if found else empty list
        """
        with open(self.filename, encoding='UTF8') as file:
            lines = []
            for line in file:
                lines.append(line)
        return lines

    def parse_lines(self, lines):
        """
        Parse the lines and returns the parsed lines if any or empty list
        :param lines: a list of lines
        :return: list of parsed lines
        """
        parsed_lines = []
        for line in lines:
            logged_line = self.line_parser.parse_line(line)
            if logged_line is None:
                continue
            parsed_lines.append(logged_line)
        return parsed_lines

    def run(self, args):
        """
        Run the parser
        :return: True if everything went fine else False
        """
        self.parse_parameters(args[1:])
        if not os.path.isfile(self.filename):
            print(f'File does not exist: {self.filename}')
            return False
        lines = self.read_lines_from_file()
        self.parsed_lines = self.parse_lines(lines)
        self.csv_file.write(self.parsed_lines)
        print(f'File {self.csv_file.filename} was created')
        return True
