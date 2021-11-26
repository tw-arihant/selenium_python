# selenium_python
**Pre requisite:** <br>
Python 3 <br>
IDE - any


-------------------------------------------------------------------------
python version 3.8 or above
create venv of python
```
python3 -m venv venv
```
Install the requirements mentioned in the script
```
pip install -r requirements.txt
```

**To run use cmd** 
```
pytest -v -s location/test_name --browser=browsername
```
Default browser = Chrome

Example: 
```
pytest -s -v testCases/test_login.py --browser=chrome
```