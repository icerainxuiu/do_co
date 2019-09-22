# 导入日志工具
import logging


# 在日志打印之前,设置日志的级别
logging.basicConfig(level=0)

# 打印五个级别的日志
logging.debug("这是个调试信息")
logging.info("这是个info信息")
logging.warning("这是个警告信息")
logging.error("这是个错误信息")
logging.critical("这是个重大错误信息")
