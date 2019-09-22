# 每日生成一个日志文件
import logging
import time
from logging import handlers

logger = logging.getLogger("haha")
# 创建日志器
# fh = handlers.TimedRotatingFileHandler('./a.log', encoding='utf-8')
logger.setLevel(logging.DEBUG)
# 创建处理器

# tfh = logging.handlers.TimedRotatingFileHandler('time.log', when='s', interval=20, backupCount=1, encoding='utf-8')
tfh = logging.handlers.TimedRotatingFileHandler("time.log", when='s', interval=20, backupCount=3, encoding="utf-8")

# 创建格式器
formatter = logging.Formatter(
    fmt="%(asc_time)s  %(level_name)s  [%(name)s]  "
    "[%(filename)s(%(funcName)s:%(line_no)d)]  -  %(message)s")
# 格式化器 放入 处理器
tfh.setFormatter(formatter)
# 处理器 放入 日志器
logger.addHandler(tfh)
# 产生日志
while True:
    logger.debug('this is a debug')
    time.sleep(10)
