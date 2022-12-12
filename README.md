# Log Parser For Doxygen Warning Logs
The purpose of the log parser is to parse warning
logs generated from a doxygen run. As an output the parser
generates a csv file with the following columns:
* File 
* Name 
* Line 
* Number 
* Warning Message

The python built in unittest framework was chosen
because I didn't want to add the dependency to
pytest in such a small project.
Pylint and flake8 were used to check the code quality.
The mock module was used to mock the file system.
These are all specified in the requirements-dev.txt file.

### To install the log parser
Run from the root of the repository:
```$> pip3 install  .```

### To run this script, you need to have Python 3 installed.
From the root folder of the repository, run:
```$> python3 -m log_parser_richard -f <filename>```

### To run the unit tests for the parser
```$> pip install -e . -r requirements-dev.txt```
```$> python3 -m unittest discover tests/```

### To run pylint on the parser
```$> pip install -e . -r requirements-dev.txt```
```$> python3 -m pylint log_parser_richard```

### To run flake8 on the parser
```$> pip install -e . -r requirements-dev.txt```
```$> python3 -m flake8 src/```

### To run flake8 on the unit tests
```$> pip install -e . -r requirements-dev.txt```
```$> python3 -m flake8 tests/```
