from time import sleep
import unittest
from libs.ShareBusiness import login_C
from libs.ShareModules import InsertLog
from libs.ShareModules import Getdata
from BeautifulReport import BeautifulReport
from PO.Pagetitle import PageTitle
from PO.StaffPage.StaffList import Account
from PO.BasePage import Base

'''读取测试数据'''
staff_number = Getdata('StaffAccountList_tc', 'staff_number')
user_number = Getdata('StaffAccountList_tc', 'user_number')
phone_number = Getdata('StaffAccountList_tc', 'phone_number')
user_name = Getdata('StaffAccountList_tc', 'user_name')
nation = Getdata('Login_tc', 'nation')
name = Getdata('StaffAccountList_tc', 'name')
loginpwd = Getdata('Login_tc', 'password')
paymentpwd = Getdata('StaffAccountList_tc', 'paymentpwd')
newphone = Base.create_mobile()

class PersonnelAccountListTest(unittest.TestCase):
    """测试账号列表页面"""

    @classmethod
    def setUpClass(self):
        self.a = login_C()
        self.b = PageTitle(self.a)
        self.c = Account(self.a)

    @classmethod
    def tearDownClass(self):
        self.c.close_broser()

    def AccountListBusiness(self):
        self.b.switch_to_HomePage()
        sleep(1)
        self.b.switch_to_PersonnelPage()
        sleep(1)
        self.c.click_account_list()

    @BeautifulReport.add_img("001_check_page_fail")
    def test_001_Check_page(self):
        """
        用例一 ：检查页面是否正常
        """
        try:
            self.AccountListBusiness()
            self.assertTrue(self.c.get_new_account_txt())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('001_check_page_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('002_shop_check_fail')
    def test_002_Verify_Select_Shop_name(self):
        """
        用例二 ：验证门店名称使用全选的方式查询
        """
        try:
            self.AccountListBusiness()
            self.assertIsNotNone(self.c.verify_select_shop_query())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('002_shop_check_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('003_staff_number_fail')
    def test_003_Verify_Staff_Number(self):
        """
        用例三 ：验证工号查询
        """
        try:  # 传参 需要查询的工号
            self.AccountListBusiness()
            self.assertTrue(self.c.verify_work_number_query(staff_number))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('003_staff_number_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('004_user_number_fail')
    def test_004_Verify_User_Number(self):
        """
        用例四 ：验证用户编号查询
        """
        try:  # 传参 需要查询的用户编号
            self.AccountListBusiness()
            self.assertTrue(self.c.verify_user_number_query(user_number))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('004_user_number_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('005_phone_number_fail')
    def test_005_Verify_Phone(self):
        """
        用例五 ：验证手机号码查询
        """
        try:  # 传参 需要查询的手机号码
            self.AccountListBusiness()
            self.assertTrue(self.c.verify_telephone_query(phone_number))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('005_phone_number_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('006_name_search_fail')
    def test_006_Verify_Name(self):
        """
        用例六 ：验证姓名查询
        """
        try:  # 传参需要查询的姓名
            self.AccountListBusiness()
            self.assertTrue(self.c.verify_name_query(user_name))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('006_name_search_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('007_reset_fail')
    def test_007_Verify_Reset(self):
        """
        用例七 ：验证重置功能
        """
        try:  # 传参任意,先输入工号,点击重置
            self.AccountListBusiness()
            self.assertIn('', self.c.verify_reset_function(user_number))  # 重置成功则返回空字符串
        except (BaseException, AssertionError) as msg:
            self.c.save_img('007_reset_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('008_edit_fail')
    def test_008_Verify_Modify_Success(self):
        """
        用例八 ：验证修改成功
        """
        try:
            self.AccountListBusiness()
            self.assertTrue(self.c.verify_modify_function())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('008_edit_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('009_add_account_fail')
    def test_009_Add_Account(self):
        """
        用例九 ：新增账号
        """
        try:  # 传参国家和对应的手机号码,姓名,登陆密码,支付密码
            self.AccountListBusiness()
            self.assertTrue(self.c.add_account(nation, newphone, name, loginpwd, paymentpwd))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('009_add_account_fail')
            InsertLog().debug(msg)
            raise BaseException


if __name__ == '__main__':
    unittest.main(verbosity=2)