# alphavantage-api-automation

This API returns the annual and quarterly income statements for the company of interest. Data is generally refreshed on the same day a company reports its latest earnings and financials.

## Getting Started

Please follow below instruction for local setup of project and Test Cases

### Software Installing
```
Install Git 
Install Python 3.x
Install latest PyCharm Or any Supported IDE
```

### GitHub and Project Setup
```
$ git clone https://github.com/anup87yadav/alphavantage-api-automation.git
$ cd alphavantage-api-automation
$ git pull origin
$ pip install -r requirements.txt
```

### Running the tests

Execute the beow commands to run test with console output
```
pytest -v --capture=no  test/test_api.py --html=report/report.html --self-contained-html

```

Execute the below commands without console output
```
pytest -v -s --capture sys test/test_api.py --html=report/report.html --self-contained-html

```
### Report

Open /report/report.html as browser to see the test run status

### Manual Test

Manual Test case Available- under folder manualtestcase
