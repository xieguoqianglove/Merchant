from time import sleep
import unittest
from PO.LoginRegisterPage.ForegotPassword import ForegotPasswordPage
from libs.ShareModules import InsertLog
from libs.ShareModules import Getdata
from BeautifulReport import BeautifulReport
'''读取测试数据'''
brand = Getdata('Login_tc', 'brand_name')
nation = Getdata('Login_tc', 'nation')
phone = Getdata('Login_tc', 'phone')
pwd = Getdata('Login_tc', 'password')

class ForegotPasswordTest(unittest.TestCase):
    """测试忘记密码"""

    def setUp(self):
        self.a = ForegotPasswordPage()

    def tearDown(self):
        sleep(5)
        self.a.close_broser()

    @BeautifulReport.add_img('001_Foregot_Password_fail')
    def test_001_Foregot_Password_Success(self):
        """
        用例一：修改登陆密码
        """
        try:
            self.a.open_url('https://buy-fat-2.pundix.com/#/findPwd/?path=test')
            self.a.input_brand_name(brand)
            self.a.setect_nation(nation, phone)
            self.a.input_code_and_next()
            self.a.input_eamil_code()
            self.assertTrue(self.a.set_login_password(pwd))
        except (BaseException, AssertionError) as msg:
            self.a.save_img('001_Foregot_Password_fail')
            InsertLog().debug(msg)
            raise BaseException

if __name__ == '__main__':
    unittest.main(verbosity=2)