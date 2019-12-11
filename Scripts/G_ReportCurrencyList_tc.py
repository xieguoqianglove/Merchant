from time import sleep
import unittest
from libs.ShareBusiness import login_C
from libs.ShareModules import InsertLog
from PO.Pagetitle import PageTitle
from PO.ReportFormPage.DigitalCurrencyRecordList import DigitalCurrencyRecord
from libs.ShareModules import Getdata
from BeautifulReport import BeautifulReport
'''读取测试数据'''
shop_name = Getdata('OrderList_tc', 'shop_name')
start_day = Getdata('ReportCashList_tc', 'start_day')
end_day = Getdata('ReportCashList_tc', 'end_day')
order_number = Getdata('ReportCurrencyList_tc', 'order_number')

class DigitalCurrencyRecordListTest(unittest.TestCase):
    """报表--数字货币记录 页面"""

    @classmethod
    def setUpClass(self):
        self.a = login_C()
        self.b = PageTitle(self.a)
        self.c = DigitalCurrencyRecord(self.a)

    @classmethod
    def tearDownClass(self):
        self.c.close_broser()

    def DigitalCurrencyRecordList(self):
        self.b.switch_to_HomePage()
        sleep(1)
        self.b.switch_to_ReportFormPage()
        sleep(1)
        self.c.click_DigitalCurrencyRecordList()

    @BeautifulReport.add_img("001_Currency_page_fail")
    def test_001_Check_Cash_page(self):
        """
        用例一 ：检查数字货币记录页面是否正常
        """
        try:
            self.DigitalCurrencyRecordList()
            self.assertTrue(self.c.get_Digital_record_msg_txt())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('001_Currency_page_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img("002_input_shop_fail")
    def test_002_Verify_Input_Shop_Name(self):
        """
        用例二 ：验证数字货币记录>门店名称使用输入的方式查询
        """
        try:  # 传参 需要查询的门店名称
            self.DigitalCurrencyRecordList()
            sleep(1)
            self.assertTrue(self.c.verify_input_shop_query(shop_name))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('002_input_shop_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('003_select_shop_fail')
    def test_003_Verify_Select_Shop_name(self):
        """
        用例三 ：验证数字货币记录>门店名称使用全选的方式查询
        """
        try:
            self.DigitalCurrencyRecordList()
            self.assertIn(shop_name, self.c.verify_select_shop_query())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('003_select_shop_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('004_reset_fail')
    def test_004_Verify_Reset(self):
        """
        用例四 ：验证数字货币记录>重置功能
        """
        try:  # 传参,先输入开始日期,点击重置
            self.DigitalCurrencyRecordList()
            self.assertIn('', self.c.verify_reset_function(start_day))  # 重置成功则返回空字符串
        except (BaseException, AssertionError) as msg:
            self.c.save_img('004_reset_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('005_Day_fail')
    def test_005_Verify_Day_Query(self):
        """
        用例五 ：验证数字货币记录>日期查询功能
        """
        try:  # 传参 开始日期和结束日期,只能输入比当前日期前一天的时间
            self.DigitalCurrencyRecordList()
            self.assertIsNotNone(self.c.verify_day_query(start_day, end_day))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('005_Day_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('006_order_number_fail')
    def test_006_Verify_Day_Query(self):
        """
        用例六 ：验证订单号查询功能
        """
        try:  # 传参 订单号
            self.DigitalCurrencyRecordList()
            self.assertTrue(self.c.verify_order_number(order_number))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('006_order_number_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('007_cashier_fail')
    def test_008_Verify_Cashier(self):
        """
        用例七 ：验证收银员查询功能
        """
        try:
            self.DigitalCurrencyRecordList()
            self.assertIsNotNone(self.c.verify_cashier())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('007_cashier_fail')
            InsertLog().debug(msg)
            raise BaseException

if __name__ == '__main__':
    unittest.main(verbosity=2)