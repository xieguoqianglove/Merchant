from PO.LoginRegisterPage.LoginPage import LoginPage
from libs.ShareModules import Getdata

#-------------------------------------------------------------------------------
# 函数/过程名称：login_B
# 函数/过程的目的：登录业务函数
#-------------------------------------------------------------------------------

band = Getdata('Login_tc', 'brand_name')  # 邮箱地址
email = Getdata('Login_tc', 'email')  # 邮箱地址
phone = Getdata('Login_tc', 'phone')  # 邮箱地址
pwd = Getdata('Login_tc', 'password') # 密码

def login_B(band='21100',email='03657303@qq.com',pwd='Abc123456'):
    obj = LoginPage()
    obj.open_url()
    obj.email_login(band, email, pwd)
    return obj.driver  # 返回一个浏览器对象 create__browser_driver 模块下的driver

def login_C(band='21100', nation='Venezuela', phone='4121999999',pwd='Abc123456'):
    obj = LoginPage()
    obj.open_url()
    obj.phone_login(band, nation, phone, pwd)
    return obj.driver  # 返回一个浏览器对象 create__browser_driver 模块下的driver



if __name__ == "__main__":
    login_C()
