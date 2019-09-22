# 将日志信息同时输出到控制台和文件中
import logging

# 创建日志器
logger = logging.getLogger("hahaha")
# 设置日志输出级别
# logging.basicConfig(level=logging.DEBUG)
logger.setLevel(logging.DEBUG)
# 创建处理器--终端处理器对象
sh = logging.StreamHandler()
# 创建处理器--文件处理器对象
fh = logging.FileHandler("./a.log")

# 创建格式器
fmt = "%(asctime)s  %(levelname)s  [%(name)s]  [%(filename)s(%(funcName)s:%(lineno)d)]  -  %(message)s"

formatter = logging.Formatter(fmt)
# 把格式器 放入 处理器
sh.setFormatter(formatter)

fh.setFormatter(formatter)
# 处理器 放入 日志器
logger.addHandler(sh)
logger.addHandler(fh)

# 产生日志
# 打印五个级别的日志
logger.info("你好啊")
logger.debug(" 我很帅吗")
logger.warning("你很帅")
logger.error("thank you")
logger.critical("yes i know")