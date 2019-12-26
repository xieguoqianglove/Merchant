from time import sleep
import unittest
from libs.ShareBusiness import login_C
from libs.ShareModules import InsertLog
from PO.Pagetitle import PageTitle
from PO.SettingPage.TimeOrFeeList import Setting
from libs.ShareModules import Getdata
from BeautifulReport import BeautifulReport
from PO.BasePage import Base
'''读取测试数据'''
fees_name = Base.create_unicode()
service_charge = Getdata('Setting_tc', 'service_charge')
tax = Getdata('Setting_tc', 'tax')

class SettingPageList(unittest.TestCase):
    """设置：时区设置、费用管理、结算货币"""

    @classmethod
    def setUpClass(self):
        self.a = login_C()
        self.b = PageTitle(self.a)
        self.c = Setting(self.a)

    @classmethod
    def tearDownClass(self):
        # sleep(10)
        self.c.close_broser()

    @BeautifulReport.add_img("Setting_001_setting_fail")
    def test_001_Click_Setting_Page(self):
        """
        用例一 ：检查设置页面是否正常
        """
        try:
            self.b.switch_to_SettingPage()
            self.assertTrue(self.c.click_setting())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('Setting_001_setting_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img("Setting_002_chang_timezone_fail")
    def test_002_Change_Time_Zone_Page(self):
        """
        用例二 ：修改时区设置
        """
        try:
            self.b.switch_to_SettingPage()
            self.assertTrue(self.c.update_time_zone())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('Setting_002_chang_timezone_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img("Setting_003_add_fees_fail")
    def test_003_Add_Fees_Tax_Page(self):
        """
        用例三 ：添加费用管理
        """
        try:
            self.b.switch_to_SettingPage()
            self.assertTrue(self.c.add_fees_tax(fees_name, service_charge, tax))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('Setting_003_add_fees_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img("Setting_004_modify_fees_fail")
    def test_004_Modify_Fees_Tax_Page(self):
        """
        用例四 ：修改费用管理
        """
        try:
            self.b.switch_to_SettingPage()
            self.assertTrue(self.c.update_fees_tax())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('Setting_004_modify_fees_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img("Setting_005_delete_fees_fail")
    def test_005_Delete_Fees_Tax_Page(self):
        """
        用例五 ：删除费用管理
        """
        try:
            self.b.switch_to_SettingPage()
            self.assertTrue(self.c.delete_fees_tax())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('Setting_005_delete_fees_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img("Setting_006_dai_crypto_fail")
    def test_006_Setting_Crypto_DAI_Page(self):
        """
        用例六 ：结算货币切换成DAI
        """
        try:
            self.b.switch_to_SettingPage()
            self.assertTrue(self.c.setting_crypto('DAI'))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('Setting_006_dai_crypto_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img("Setting_007_usdt_crypto_fail")
    def test_007_Setting_Crypto_USDT_Page(self):
        """
        用例七 ：结算货币切换成USDT
        """
        try:
            self.b.switch_to_SettingPage()
            self.assertTrue(self.c.setting_crypto('USDT'))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('Setting_007_usdt_crypto_fail')
            InsertLog().debug(msg)
            raise BaseException

if __name__ == '__main__':
    unittest.main(verbosity=2)