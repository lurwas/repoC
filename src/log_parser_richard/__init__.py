"""
The Log Parser Module
"""
import sys
from log_parser_richard.log_parser import LogParser

if __name__ == '__main__':
    parser = LogParser()
    run_result = parser.run(sys.argv)
    if not run_result:
        sys.exit(2)
