import logging

class LogGenerator():
    @staticmethod
    def logenerator():
        logging.basicConfig(filename=r"C:\Users\sudha\PycharmProjects\SWIFT PROTECT HYBRID\Logs\Swift.log",
                        format='%(asctime)s: %(levelname)s: %(message)s',
                        datefmt='%m/%d/%y %I:%M:%S %p',
                        force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger