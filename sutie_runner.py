# 组织运行测试用例
import time
import unittest
from case.test02_tester_create_bug import TestTesterCreateBug
from config import BASE_PATH
# 创建测试套件


suite = unittest.TestSuite()

# 组织测试用例
suite.addTest(unittest.makeSuite(TestTesterCreateBug))

# 创建运行器
# verbosity -- 控制执行结果打印详细程度
# stream -- 可以把执行的结果保存到外部文件流

filename = BASE_PATH+"/report/report_{}.txt".format(time.strftime("%Y%m%d%H%M%S"))
# 打开外部的文件
with open(filename, 'w') as f:
    # 外部文件中写入测试结果数据
    runner = unittest.TextTestRunner(stream=f, verbosity=2)
    # 执行测试套件
    runner.run(suite)
