"""
Entry point for the Log Parser Module
"""
import sys
from log_parser_richard.log_parser import LogParser


def main():
    """Main function"""
    parser = LogParser()
    # Since pylint sees every variable in __init__
    # as a constant, we need to disable the warning
    # pylint: disable=invalid-name
    result = parser.run(sys.argv)
    if not result:
        sys.exit(2)


if __name__ == '__main__':
    main()
