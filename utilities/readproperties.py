import configparser

config = configparser.RawConfigParser()
config.read("configurations/config.ini")


class ReadConfig:
    @staticmethod
    def geturl():
        url = config.get('info', 'baseURL')
        return url

    @staticmethod
    def getkey():
        apikey = config.get('info', 'apiKey')
        return apikey
