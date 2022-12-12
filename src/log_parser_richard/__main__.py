"""
Entry point for the Log Parser Module
"""
import sys
from log_parser_richard.log_parser import LogParser


def main():
    """Main function"""
    parser = LogParser()
    result = parser.run(sys.argv)
    if not result:
        sys.exit(2)


if __name__ == '__main__':
    main()
