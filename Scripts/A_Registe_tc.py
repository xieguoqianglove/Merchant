import time
import unittest
from PO.LoginRegisterPage.RegisterPage import RegisterPage
from libs.ShareModules import InsertLog
from libs.ShareModules import Getdata
from BeautifulReport import BeautifulReport
from PO.BasePage import Base

'''读取测试数据'''
brand_name = Getdata('Registe_tc', 'brand_name')
nation = Getdata('Registe_tc', 'nation')
loginpwd = Getdata('Registe_tc', 'loginpwd')
name = Getdata('Registe_tc', 'name')
surname = Getdata('Registe_tc', 'surname')
imei = Getdata('Registe_tc', 'imei')
paymentpwd = Getdata('Registe_tc', 'paymentpwd')
email = Base.create_email()
phone_number = Base.create_mobile()

class RegisteTest(unittest.TestCase):
    """测试 注册页面"""
    def setUp(self):
        self.a = RegisterPage()

    def tearDown(self):
        time.sleep(30)
        self.a.close_broser()

    @BeautifulReport.add_img('001_Register_Fail')
    def test_001_Register_Business(self):
        """
        :param brandname: 品牌名称
        :param nation:    国家名称
        :param Phone:   手机号码
        :param loginpwd:  登录密码
        :param name:  名字
        :param surname: 姓
        :param imei:  imei号
        :param Email: 邮箱
        :param paymentpwd: 支付密码
        """
        try:
            # self.a.click_registration()
            self.a.open_url('https://buy-fat-1.pundix.com/#/register/?path=test')
            self.a.select_business_category()  # 选择经营品类，默认选择 Government
            self.a.set_brand_name(brand_name)  # 输入品牌名称
            self.a.input_login_password(loginpwd, name, surname)  # 输入登陆密码、名、姓
            self.a.select_time_zone()  # 选择时区
            self.a.input_imei(imei)  # 输入Imei
            self.a.input_email_address(email)  # 输入邮箱
            self.a.input_payment_password(paymentpwd)  # 输入支付密码、确认支付密码
            self.a.setect_nation(nation, phone_number)  # 选择国家、输入号码、验证码
            self.a.click_regisetr_laction()  # 点击注册
            self.a.click_return_login()      # 点击返回登陆
        except (BaseException, AssertionError) as msg:  # BaseException所有异常的基类,AssertionError断言语句失败
            InsertLog().debug(msg)
            self.a.save_img('001_Register_Fail')
            raise BaseException


if __name__ == '__main__':
    unittest.main(verbosity=2)
