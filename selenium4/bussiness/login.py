import time
import yaml,os
path=os.getcwd()
class Login_tes:#登录模块封装
    def __init__(self,driver):#
        self.driber=driver

        self.file=open(r'C:\Users\cheng\PycharmProjects\selenium4\data\page_data.yaml', "r",encoding= "utf-8")
        self.data=yaml.load(self.file)
        self.file.close()
        self.lo_url=self.data['login'].get('url')
        self.denglu=self.data['login'].get('denglu')
        self.username=self.data['login'].get('name')
        self.password=self.data['login'].get('password')
        self.sub=self.data['login'].get('denglu_btm')
        # self.lo_err=self.data['login'].get('login_err')
        self.lo_suc=self.data['login'].get('login_suc')
        self.driber.get(self.lo_url)
    def login(self,suc,name,password):
        try:
            time.sleep(2)

            self.driber.find_element_by_id(self.username).clear()
            self.driber.find_element_by_id(self.username).send_keys(name)
            self.driber.find_element_by_id(self.password).click()
            self.driber.find_element_by_id(self.password).send_keys(password)
            self.driber.find_element_by_class_name(self.sub).click()
            time.sleep(3)
            if suc=='1':
                 self.login_su = self.driber.find_element_by_xpath(self.lo_suc).text
                 print('成功')
                 time.sleep(5)
                 return self.login_su
            if suc=='0':
                self.login_err=self.driber.find_element_by_xpath(self.sub).text
        except Exception as e:
            print(e)
        finally:
            print('该关闭浏览器了')
            self.driber.quit()