import logging
import os

# 项目配置文件

# 项目根目录
from logging.handlers import TimedRotatingFileHandler

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


# print(BASE_PATH)


# 定义日志配置方法
def set_log():
    # 日志器, 处理器, 格式化器
    # 处理器设置格式化器 , 日志器添加处理器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 2. 创建处理器  终端  时间分割文件
    shl = logging.StreamHandler()
    trfl = TimedRotatingFileHandler(filename=BASE_PATH + "/log/myLog.log", when="midnight", interval=1, backupCount=5,
                                    encoding="utf-8")

    # 3. 创建格式化器
    fmtter = logging.Formatter(fmt="%(asctime)s %(levelname)s [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")

    # 4.给处理器设置格式化器
    shl.setFormatter(fmtter)
    trfl.setFormatter(fmtter)

    # 5.给日志器添加处理器
    logger.addHandler(shl)
    logger.addHandler(trfl)
