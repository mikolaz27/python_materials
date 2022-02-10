import sys
import time


class Logger:

    def __init__(self):
        self.format = '%Y-%b-%d %H:%M:%S -->'

    def log(self, message):
        current_time = time.localtime()
        sys.stderr.write(
            f"{time.strftime(self.format, current_time)} --> {message}\n")


logger = Logger()
logger.log('An error has happened!')


class DateLogger(Logger):
    def __init__(self):
       super().__init__()
       self.format = '%Y-%b-%d -->'

logger2 = DateLogger()
logger2.log('An error has happened!')