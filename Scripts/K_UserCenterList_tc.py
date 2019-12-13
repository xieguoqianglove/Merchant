from time import sleep
import unittest
from libs.ShareBusiness import login_C
from libs.ShareModules import InsertLog
from PO.Pagetitle import PageTitle
from PO.UserCenterPage.UserCenterList import UserCenterList
from libs.ShareModules import Getdata
from BeautifulReport import BeautifulReport
'''读取测试数据'''
newloginpwd = Getdata('UserCenterList_tc', 'newloginpwd')
newpaypwd = Getdata('UserCenterList_tc', 'newpaypwd')

class ZPersonalCentPasswordList(unittest.TestCase):
    """个人中心: 修改支付密码、登录密码、用户信息、退出"""

    @classmethod
    def setUpClass(self):
        self.a = login_C()
        self.b = PageTitle(self.a)
        self.c = UserCenterList(self.a)

    @classmethod
    def tearDownClass(self):
        sleep(20)
        self.c.close_broser()

    @BeautifulReport.add_img("001_User_info_fail")
    def test_001_Click_User_Information_Page(self):
        """
        用例一 ：检查用户信息页面是否正常
        """
        try:
            self.b.switch_to_Personal_CenterPage()
            self.assertTrue(self.c.click_user_information())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('001_User_info_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img("002_chang_loginpwd_fail")
    def test_002_Change_Login_Password_Page(self):
        """
        用例二 ：修改登录密码功能
        """
        try:  # 传参原密码、新密码、确认密码，判断出现新密码和旧密码一样的提示语，断言成功
            self.b.switch_to_Personal_CenterPage()
            self.assertTrue(self.c.click_login_password(newloginpwd, newloginpwd))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('002_chang_loginpwd_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img("003_chang_paypwd_fail")
    def test_003_Change_Payment_Password_Page(self):
        """
        用例三 ：修改支付密码功能
        """
        try:  # 传参原密码、新密码、确认密码，判断出现新密码和旧密码一样的提示语，断言成功
            self.b.switch_to_Personal_CenterPage()
            self.assertTrue(self.c.click_payment_password(newpaypwd, newpaypwd))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('003_chang_paypwd_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img("004_exit_fail")
    # @unittest.skip('跳过')
    def test_004_Click_Exit_Login_Page(self):
        """
        用例四 ：检查退出登录功能是否正常
        """
        try:  # 点击退出登录后，判断页面是否出现 '商家后台系统'文本
            self.b.switch_to_Personal_CenterPage()
            self.assertTrue(self.c.click_exit_login())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('004_exit_fail')
            InsertLog().debug(msg)
            raise BaseException


if __name__ == '__main__':
    unittest.main(verbosity=2)