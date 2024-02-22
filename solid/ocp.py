# Open Close Principe
import sys
import time


# Problem
class Logger:

    def log(self, message):
        current_time = time.localtime()
        sys.stderr.write(
            f"{time.strftime('%Y-%b-%d %H:%M:%S -->', current_time)} --> {message}\n")


# logger = Logger()
# logger.log('An error has happened!')

# Solution
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

logger_with_date = DateLogger()
logger_with_date.log('An error has happened!')
