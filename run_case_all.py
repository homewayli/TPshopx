
# 导入包
import unittest
import HTMLTestRunnerPlugins
import time
# 1 获取测试用例文件夹路径
case_dir = './scripts'
# 2 获取需要执行测测试用例文件.py

# 3 建立测试报告存放路径
report_dir = './report'
# 4 将需要执行的测试用例添加到测试套件中
discover = unittest.defaultTestLoader.discover(case_dir,pattern='test_*.py')
# 5 使用HTMLTestRunnerPlugins执行测试用例并生测试报告
# 5.1 给测试报告命名
now = time.strftime("%Y_%m_%d %H_%M_%S")
# with open(report_dir+'\\'+now+'report.html','wb') as fp:
file = open(report_dir+'\\'+now+'report.html','wb')

# 5.2 执行测试
runner = HTMLTestRunnerPlugins.HTMLTestRunner(
                                      title="ECshop自动化测试报告",
                                      description="报告详细描述",
                                      verbosity=2,
                                      stream=file,
                                      retry=0
                                        )
runner.run(discover)
file.close()
