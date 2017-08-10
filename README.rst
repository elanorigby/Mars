Mars Mission Control
####################

To run this application
-----------------------
* cd into rover directory
* run
  * `$ python3 mission/rover.py <'path/to/input/file'>`
  * `$ python3 mission/rover.py 'instructions/file1.txt'` for example


To run the tests for this application
-------------------------------------
* cd into rover directory
* create and activate a virtual environment that uses Python 3
* run
  * `$ pip install pipenv` - this will install requirements in the Pipfile
  * `$ pipenv shell` - this will open a shell for the virtual environment
* testing options
  * (in shell) run
  * `$ pytest` - this will run all tests in minimized mode, a string of dots
  * `$ pytest -v` - this will run all tests in verbose mode
