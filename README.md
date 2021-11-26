# selenium_python
**Pre requisite:** <br>
Python 3 <br>
IDE - any


-------------------------------------------------------------------------

Create venv of python
```
python3 -m venv venv
```
Activate the venv
```
./venv/bin/activate
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
pytest -s -v testCases/test_login.py
```