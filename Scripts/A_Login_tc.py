from time import sleep
import unittest
from PO.LoginRegisterPage.LoginPage import LoginPage
from libs.ShareModules import InsertLog
from libs.ShareModules import Getdata
from BeautifulReport import BeautifulReport
'''读取测试数据'''
brand = Getdata('Login_tc', 'brand_name')
email = Getdata('Login_tc', 'email')
nation = Getdata('Login_tc', 'nation')
phone = Getdata('Login_tc', 'phone')
pwd = Getdata('Login_tc', 'password')

class LoginTest(unittest.TestCase):
    """测试登录功能"""

    def setUp(self):
        self.a = LoginPage()
        self.a.open_url()

    def tearDown(self):
        # sleep(40)  # 防止提示验证码发送过快
        sleep(5)
        self.a.close_broser()

    @BeautifulReport.add_img('LoginTest_001_phone_login_fail')
    def test_001_Login_Success(self):
        """
        用例一：手机号登陆
        """
        try:  # 传参品牌名,邮箱,登录密码

            self.a.phone_login(brand, nation, phone, pwd)
            self.assertTrue(self.a.login_success_msg())
        except (BaseException, AssertionError) as msg:
            self.a.save_img('LoginTest_001_phone_login_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('LoginTest_002_email_login_fail')
    def test_002_Email_login(self):
        """
        用例二： 邮箱登陆
        """
        try:  # 传参品牌名,邮箱,登录密码

            self.a.email_login(brand, email, pwd)
            self.assertTrue(self.a.login_success_msg())
        except (BaseException, AssertionError) as msg:
            self.a.save_img('LoginTest_002_email_login_fail')
            InsertLog().debug(msg)
            raise BaseException


if __name__ == '__main__':
    unittest.main(verbosity=2)