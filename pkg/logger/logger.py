import logging
from logging.handlers import TimedRotatingFileHandler


log_level_setting = {
    0: logging.DEBUG,
    1: logging.INFO,
    2: logging.WARNING,
    3: logging.ERROR,
    4: logging.CRITICAL
}

class Logger:
    def __init__(self, file, level):
        # 设置日志级别
        if level > 5 or level < 0:
            raise ValueError("The log level does not meet the specifications！")

        # 创建一个 logger，并设置 logger级别
        self.logger = logging.getLogger()
        self.logger.setLevel(log_level_setting[level])

        # 创建一个handler，用于写入日志文件
        self.file = file
        # when参数用于指定TimedRotatingFileHandler的滚动时间间隔。它接受以下几种常用的参数：
        #
        # 'midnight': 在每天午夜（即0点）滚动日志文件。
        # 'S': 每秒钟滚动一次日志文件。
        # 'M': 每分钟滚动一次日志文件。
        # 'H': 每小时滚动一次日志文件。
        # 'D': 每天滚动一次日志文件。
        # 'W0' 到 'W6': 每周指定的星期几滚动一次日志文件，其中 'W0' 表示星期天，'W1' 表示星期一，依此类推。
        # self.handler = TimedRotatingFileHandler('test.log',when='S')
        self.handler = TimedRotatingFileHandler('test.log', when='midnight')
        self.handler.setLevel(log_level_setting[level])
        self.logger.addHandler(self.handler)

        # 定义handler 的输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(process)d - %(thread)d - %(filename)s - %(funcName)s - %(lineno)d - %(message)s')
        self.handler.setFormatter(self.formatter)

        if level ==1:
            # 在创建一个handler，用于输入控制台
            self.console_handler = logging.StreamHandler()
            self.console_handler.setLevel(level)
            self.logger.addHandler(self.console_handler)
            self.console_formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s')
            self.console_handler.setFormatter(self.console_formatter)


    def debug(self, message):
        self.handler.flush()
        self.logger.debug(message)
    def info(self, message):
        self.handler.flush()
        self.logger.info(message)
    def warning(self, message):
        self.handler.flush()
        self.logger.warning(message)
    def error(self, message):
        self.handler.flush()
        self.logger.error(message)
    def critical(self, message):
        self.handler.flush()
        self.logger.critical(message)
