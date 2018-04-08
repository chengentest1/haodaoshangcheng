import os
import time
import unittest

from package.HTMLTestRunner import HTMLTestRunner

if __name__=='__main__':
    now=time.strftime('%Y-%m-%d %H-%M-%S')
   # path=os.path.dirname(__file__)
    filename='./report/'+now+'result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='海盗商城自动化测试报告',description='浏览器：Chrome 环境：window10')

    discover=unittest.defaultTestLoader.discover(r'.\testcase',pattern='*_test_suite.py')
    runner.run(discover)



    fp.close()

    #print(path)