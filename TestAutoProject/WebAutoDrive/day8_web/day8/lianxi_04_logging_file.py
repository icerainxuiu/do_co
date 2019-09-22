# 导入日志工具

# 在日志打印之前,设置日志的输出文件
# logging.basicConfig(level=logging.DEBUG)
import logging

fmt = "%(asc_time)s  %(level_name)s  [%(name)s]  [%(filename)s(%(funcName)s:%(line_no)d)]  -  %(message)s"

logging.basicConfig(
    format=fmt,
    filename='.log'.encode('utf-8'),
    level=logging.INFO)

# 打印五个级别的日志
logging.debug("这是个调试信息")
logging.info("这是个info信息")
logging.warning("这是个警告信息")
logging.error("这是个错误信息")
logging.critical("这是个重大错误信息")
