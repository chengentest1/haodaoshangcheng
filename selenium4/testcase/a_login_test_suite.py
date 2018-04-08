import os
import unittest

import ddt
import time

from bussiness.login import Login_tes
from untils.gettestdata import huoqu_test
from selenium import webdriver

from untils.log import LOG

path=os.getcwd()
case_path=r'C:\Users\cheng\PycharmProjects\selenium4\data\case1.xlsx'
casedata=huoqu_test(case_path,0)
@ddt.ddt
class Logintest(unittest.TestCase):

    def setUp(self):

        self.deriver= webdriver.Chrome()
        self.logs=Login_tes(self.deriver)
        time.sleep(3)
        LOG.info('login测试用例开始执行')
    @ddt.data(*casedata)
    def test_login(self,casedata):
        self.user=casedata['username']
        self.passw = casedata['pwd']
        self.suc=casedata['suc']
        self.assert_v=casedata['assert']
        self.assert_return=self.logs.login(suc=self.suc,name=self.user,password=self.passw)
        LOG.info('登录测试，传入参数:用户名：%s，密码：%s,返回结果：%s'%(self.user,self.passw,self.assert_return))
        self.assertEqual(self.assert_v, self.assert_return,msg='fail resons:%s !=%s'%(self.assert_v,self.assert_return))
    def tearDown(self):
        LOG.info('测试用例执行完毕，测试环境正在还原！')
        self.deriver.quit()



if __name__=="__main__":
    unittest.main()