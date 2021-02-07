from ratelimit import limits, rate_limited, sleep_and_retry
import time
from test.test_base import TestBase


class TestAPI(TestBase):
    ONE_DAY = 3600 * 24
    ONE_MINUTE = 60

    ''' Verify the response status code'''

    @sleep_and_retry
    @rate_limited(calls=500, period=ONE_DAY)
    @sleep_and_retry
    @rate_limited(calls=5, period=ONE_MINUTE)
    def test_verifystatusCode(self):
        self.resp = TestBase().apicall()
        assert self.resp.status_code == 200, "not valid code"
        # uncomment below line if you want to see output in console section
        # print(self.resp.status_code)

    '''Verify the Response Content-Type'''

    @sleep_and_retry
    @rate_limited(calls=500, period=ONE_DAY)
    @sleep_and_retry
    @rate_limited(calls=5, period=ONE_MINUTE)
    def test_verifyheaders(self):
        self.resp = TestBase().apicall()
        # uncomment below line if you want to see output in console section
        # print(self.resp.headers.get("Content-Type"))
        assert self.resp.headers.__contains__("Content-Type")

    '''Verify the URL'''

    @sleep_and_retry
    @rate_limited(calls=500, period=ONE_DAY)
    @sleep_and_retry
    @rate_limited(calls=5, period=ONE_MINUTE)
    def test_verifyurl(self):
        self.resp = TestBase().apicall()
        # uncomment below line if you want to see output in console section
        # print(self.resp.url)
        assert self.resp.url == "https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey=apikey"

    '''Verify Response Time'''

    @sleep_and_retry
    @rate_limited(calls=500, period=ONE_DAY)
    @sleep_and_retry
    @rate_limited(calls=5, period=ONE_MINUTE)
    def test_verifyresponsetime(self):
        self.resp = TestBase().apicall()
        # uncomment below line if you want to see output in console section
        # print(self.resp.elapsed.total_seconds())
        assert self.resp.elapsed.total_seconds() < 200, "not valid time limit"

    '''Verify the symbol value in response body'''

    @sleep_and_retry
    @limits(calls=500, period=ONE_DAY)
    def test_verifysymbolvalue(self):
        self.resp = TestBase().apicall()
        time.sleep(1)
        body = self.resp.json()
        # uncomment below line if you want to see output in console section
        # print(body["symbol"])
        assert (body["symbol"]) == "IBM", "Not Found"

    '''Verify the reported Currency type in response body'''

    @sleep_and_retry
    @rate_limited(calls=500, period=ONE_DAY)
    @sleep_and_retry
    @rate_limited(calls=5, period=ONE_MINUTE)
    def test_verifyreportedcurrency(self):
        self.resp = TestBase().apicall()
        time.sleep(5)
        body = self.resp.json()

        """ 
        uncomment below line if you want to see output in console section
        print(body["annualReports"][0]["reportedCurrency"])
        print(body["quarterlyReports"][0]["reportedCurrency"])
        """

        assert (body["annualReports"][0]["reportedCurrency"]) == "USD"
        assert (body["quarterlyReports"][0]["reportedCurrency"]) == "USD"
