import logging


# 创建日志器
from logging import handlers

logger = logging.getLogger("tp_test")

logger.setLevel(logging.DEBUG)
# 创建处理器(文件处理器，每天生成一个新日志文件，总共30个，测试级别为debug)
dfh = handlers.TimedRotatingFileHandler("../log_tp_test/test.log", when='d',
                                        interval=1, backupCount=30, encoding='utf-8')

# 创建格式化器
formatter = logging.Formatter(fmt="%(asctime)s %(levelname)s [%(name)s] "
                                  "[%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")

# 将格式化器加入处理器
dfh.setFormatter(formatter)
# 将处理器加入日志器
logger.addHandler(dfh)
