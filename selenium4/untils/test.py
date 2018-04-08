import os

import ddt

from bussiness.login import Login_tes
from untils.gettestdata import huoqu_test
from selenium import webdriver

from untils.log import LOG

path=os.getcwd()
#case_path=path+r'\data\case1.xlsx'
case_path=r'C:\Users\cheng\PycharmProjects\selenium4\data\case1.xlsx'
casedata=huoqu_test(case_path,0)

print(casedata)

