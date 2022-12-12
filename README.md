# Log Parser For Doxygen Warning Logs

# TODO: Insert more information here
To run:

# To run the unit tests for the parser
$> pip install -e . -r requirements-dev.txt
$> python3 -m unittest discover tests/

# To run pylint on the parser
$> pip install -e . -r requirements-dev.txt
$> python3 -m pylint log_parser_richard

# To run flake8 on the parser
$> pip install -e . -r requirements-dev.txt
$> python3 -m flake8 src/

# To run flake8 on the unit tests
$> pip install -e . -r requirements-dev.txt
$> python3 -m flake8 tests/
