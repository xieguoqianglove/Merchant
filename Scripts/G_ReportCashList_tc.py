from time import sleep
import unittest
from libs.ShareBusiness import login_C
from libs.ShareModules import InsertLog
from PO.Pagetitle import PageTitle
from BeautifulReport import BeautifulReport
from PO.ReportFormPage.OverviewAndCashList import OverviewAndCash
from libs.ShareModules import Getdata
'''读取测试数据'''
shop_name = Getdata('OrderList_tc', 'shop_name')
start_day = Getdata('ReportCashList_tc', 'start_day')
end_day = Getdata('ReportCashList_tc', 'end_day')

class ReportCashRecordListTest(unittest.TestCase):
    """测试 报表--概览/现金记录 页面"""

    @classmethod
    def setUpClass(self):
        self.a = login_C()
        self.b = PageTitle(self.a)
        self.c = OverviewAndCash(self.a)

    @classmethod
    def tearDownClass(self):
        self.c.close_broser()

    def CashRecordListBusiness(self):
        self.b.switch_to_ShopPage()
        sleep(1)
        self.b.switch_to_ReportFormPage()
        sleep(1)
        self.c.click_carh_history()

    @BeautifulReport.add_img("ReportCash_001_Overview_page_fail")
    def test_001_Check_Overview_page(self):
        """
        用例一 ：检查概览页面是否正常
        """
        try:
            self.b.switch_to_ReportFormPage()
            sleep(1)
            self.c.click_OverviewList()
            self.assertTrue(self.c.get_Cash_msg_txt())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('ReportCash_001_Overview_page_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img("ReportCash_002_Cash_page_fail")
    def test_002_Check_Cash_page(self):
        """
        用例二 ：检查现金记录页面是否正常
        """
        try:
            self.CashRecordListBusiness()
            self.assertTrue(self.c.get_carh_history_txt())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('ReportCash_002_Cash_page_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img("ReportCash_003_input_shop_fail")
    def test_003_Verify_Input_Shop_Name(self):
        """
        用例三 ：验证现金记录>门店名称使用输入的方式查询
        """
        try:  # 传参 需要查询的门店名称
            self.CashRecordListBusiness()
            sleep(1)
            self.assertTrue(self.c.verify_input_shop_query(shop_name))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('ReportCash_003_input_shop_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('ReportCash_004_select_shop_fail')
    def test_004_Verify_Select_Shop_name(self):
        """
        用例四 ：验证现金记录>门店名称使用全选的方式查询
        """
        try:
            self.CashRecordListBusiness()
            self.assertIn(shop_name, self.c.verify_select_shop_query())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('ReportCash_004_select_shop_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('ReportCash_005_reset_fail')
    def test_005_Verify_Reset(self):
        """
        用例五 ：验证现金记录>重置功能
        """
        try:  # 传参,先输入开始日期,点击重置
            self.CashRecordListBusiness()
            self.assertIn('', self.c.verify_reset_function(start_day))  # 重置成功则返回空字符串
        except (BaseException, AssertionError) as msg:
            self.c.save_img('ReportCash_005_reset_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('ReportCash_006_Day_fail')
    def test_006_Verify_Day_Query(self):
        """
        用例六 ：验证现金记录>日期查询功能
        """
        try:  # 传参 开始日期和结束日期,只能输入比当前日期前一天的时间
            self.CashRecordListBusiness()
            self.assertIsNotNone(self.c.verify_day_query(start_day,end_day))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('ReportCash_006_Day_fail')
            InsertLog().debug(msg)
            raise BaseException

if __name__ == '__main__':
    unittest.main(verbosity=2)