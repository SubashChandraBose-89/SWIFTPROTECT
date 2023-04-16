import configparser

config = configparser.RawConfigParser()
config.read(r'C:\Users\sudha\PycharmProjects\SWIFT PROTECT HYBRID\Configurations\config.ini')

class ReadConfig:
    @staticmethod
    def getURL():
        url = config.get('userdata', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('userdata', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('userdata', 'password')
        return password