import requests


class TestBase:

    def apicall(self):
        q = {"function": "INCOME_STATEMENT", "symbol": "IBM", "apikey": "apikey"}
        resp = requests.get("https://www.alphavantage.co/query", params=q)
        if resp.status_code != 200:
            raise Exception('API response: {}'.format(resp.status_code))
        return resp
