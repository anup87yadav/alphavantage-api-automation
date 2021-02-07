import logging


class LogGen:
    @staticmethod
    def logger():
        logging.basicConfig(filename="/log/automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
