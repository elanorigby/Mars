Mars Mission Control
####################

To run this application
=======================
* cd into mars directory
* run `$ python3 launch.py <'path/to/input/file'>`
* example `$ python3 launch.py 'instructions/file1.txt'`


Set up for testing
==================
* cd into mars directory
* create and activate a virtual environment that uses Python 3
* run `$ pip install pipenv`
   * this will install requirements in the Pipfile
* run `$ pipenv shell`
   * this will open a shell for the virtual environment

To run the tests
----------------
* in shell run
* `$ pytest` - this will run all tests in minimized mode, a string of dots
* `$ pytest -v` - this will run all tests in verbose mode
* `$ pytest <path/to/test/file>` to run the tests in that specific file

To see test coverage
--------------------
* in shell run
* `$ coverage run launch.py 'instructions/file1.txt'`
   * this runs the app and gathers coverage data
* `$ coverage report`
   * this displays coverage data
* `$ coverage report -m`
   * this displays coverage data and line numbers where coverage is missing



