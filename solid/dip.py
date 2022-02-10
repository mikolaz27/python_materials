import sys
import time


class TerminalPrinter:
    def write(self, msg):
        sys.stderr.write(f"{msg}\n")


class FilePrinter:
    def write(self, msg):
        with open('log.txt', 'a+', encoding='UTF8') as f:
            f.write(f"{msg}\n")


class Logger:
    def __init__(self):
        self.format = time.strftime('%Y-%b-%d %H:%M:%S', time.localtime())

    def log(self, message, notifier):
        prefix = time.strftime(self.format, time.localtime())
        notifier().write(f"{prefix} {message}")

    # def log_stderr(self, message):
    #     TerminalPrinter().write(f"{self.prefix} {message}")
    #
    #
    # def log_file(self, message):
    #     FilePrinter().write(f"{self.prefix} {message}")

logger = Logger()
logger.log("Starting the program...", TerminalPrinter)
# logger.log_stderr("An error!")