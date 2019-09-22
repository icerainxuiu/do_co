# 导入日志工具


# 在日志打印之前,设置日志的格式
# logging.basicConfig(level=logging.DEBUG)
import logging

fmt = "%(asctime)s  %(levelname)s  [%(name)s]  [%(filename)s(%(funcName)s:%(lineno)d)]  -  %(message)s"

logging.basicConfig(format=fmt)
logging.debug('这是个调试信息')
logging.info("这是条普通信息")
logging.error("这是条错误信息")
logging.warning("这是条警告信息")
logging.critical("这是条严重错误信息")
# 打印五个级别的日志
