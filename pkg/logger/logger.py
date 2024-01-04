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
        if level > 4 or level < 0:
            raise ValueError("The log level does not meet the specifications！")
        self.file = file
        self.level = log_level_setting[level]
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.handler = TimedRotatingFileHandler(self.file, when='midnight')
        self.handler.setLevel(self.level)
        self.logger.addHandler(self.handler)
        self.formatter = logging.Formatter(
            f'%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s')
        self.handler.setFormatter(self.formatter)
        if level == 0:
            self.console_handler = logging.StreamHandler()
            self.console_handler.setLevel(logging.DEBUG)
            self.logger.addHandler(self.console_handler)
            self.console_formatter = logging.Formatter(
                f'%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s')
            self.console_handler.setFormatter(self.console_formatter)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


# 创建实例并使用
logger = Logger('test.log', 0)  # 0 表示 debug 级别
# 将 logger 对象导出为模块的属性
log = logger