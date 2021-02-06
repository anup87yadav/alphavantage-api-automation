import requests
import logging
from ratelimit import limits, RateLimitException, rate_limited
import time


class TestAPI:

    ONE_DAY = 3600 * 24

    ''' Verify the response status code'''
    @rate_limited(calls=500, period=ONE_DAY)
    def test_verifyStatusCode(self):
        @rate_limited(calls=5, period=60)
        def test_apicalltest():
            try:
                q = {"function": "INCOME_STATEMENT", "symbol": "IBM", "apikey": "apikey"}
                resp = requests.get("https://www.alphavantage.co/query", params=q)
                logging.info(resp)
                if resp.status_code == 429:
                    raise RateLimitException("too many calls", 60)
                assert resp.status_code == 200, "not valid code"
            except Exception as e:
                print(e)

    '''Verify the Response Content-Type'''
    @limits(calls=5, period=60)
    def test_verifyheaders(self):
        q = {"function": "INCOME_STATEMENT", "symbol": "IBM", "apikey": "apikey"}
        resp = requests.get("https://www.alphavantage.co/query", params=q)
        assert resp.headers.__contains__("Content-Type")

    '''Verify the URL'''
    @limits(calls=5, period=60)
    def test_verifyurl(self):

        q = {"function": "INCOME_STATEMENT", "symbol": "IBM", "apikey": "apikey"}
        resp = requests.get("https://www.alphavantage.co/query", params=q)
        print(resp.url)

    '''Verify Response Time'''
    @limits(calls=5, period=60)
    def test_verifyresponsetime(self):
        q = {"function": "INCOME_STATEMENT", "symbol": "IBM", "apikey": "apikey"}
        resp = requests.get("https://www.alphavantage.co/query", params=q)
        assert resp.elapsed.total_seconds() < 200, "not valid time limit"

    '''Verify the symbol value in response body'''
    @limits(calls=5, period=60)
    def test_verifysymbolvalue(self):
        q = {"function": "INCOME_STATEMENT", "symbol": "IBM", "apikey": "apikey"}
        resp = requests.get("https://www.alphavantage.co/query", params=q)
        time.sleep(1)
        body = resp.json()
        print(body["symbol"])
        print(body)
        assert (body["symbol"]) == "IBM", "Not Found"

    '''Verify the reported Currency type in response body'''
    @limits(calls=5, period=60)
    def test_verifyreportedcurrency(self):
        q = {"function": "INCOME_STATEMENT", "symbol": "IBM", "apikey": "apikey"}
        resp = requests.get("https://www.alphavantage.co/query", params=q)
        time.sleep(1)
        body = resp.json()
        assert (body["annualReports"][0]["reportedCurrency"]) == "USD"
        assert (body["quarterlyReports"][0]["reportedCurrency"]) == "USD"
