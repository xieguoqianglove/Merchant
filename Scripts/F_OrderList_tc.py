from time import sleep
import unittest
from libs.ShareBusiness import login_C
from libs.ShareModules import InsertLog
from PO.Pagetitle import PageTitle
from PO.OrderPage.OrderManagementList import OrderManagement
from libs.ShareModules import Getdata
from BeautifulReport import BeautifulReport
'''读取测试数据'''
shop_name = Getdata('ShopList_tc', 'shop_name')

class OrderManagementTest(unittest.TestCase):
    """测试 订单--订单管理 页面"""

    @classmethod
    def setUpClass(self):
        self.a = login_C()
        self.b = PageTitle(self.a)
        self.c = OrderManagement(self.a)

    @classmethod
    def tearDownClass(self):
        self.c.close_broser()

    def OrderManagermentBusiness(self):
        self.b.switch_to_ShopPage()
        sleep(1)
        self.b.switch_to_OrderPage()
        sleep(1)
        self.c.click_OrderManagement()

    @BeautifulReport.add_img("OrderTest_001_page_fail")
    def test_001_Check_page(self):
        """
        用例一 ：检查页面是否正常
        """
        try:
            self.OrderManagermentBusiness()
            self.assertTrue(self.c.findElement('Cashier Order'))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('OrderTest_001_page_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img("OrderTest_002_search_fail")
    def test_002_Verify_Input_Shop_Name(self):
        """
        用例二 ：验证门店名称使用输入的方式查询
        """
        try:  # 传参 需要查询的门店名称
            self.OrderManagermentBusiness()
            self.assertTrue(self.c.input_shop_query(shop_name))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('OrderTest_002_search_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img("OrderTest_003_search_fail")
    def test_003_Verify_Select_Shop_name(self):
        """
        用例三 ：验证门店名称使用全选的方式查询
        """
        try:
            self.OrderManagermentBusiness()
            self.assertTrue(self.c.verify_select_shop_query())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('OrderTest_003_search_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img("OrderTest_004_details_fail")
    def test_004_Verify_Modify_Function(self):
        """
        用例四 ：验证详情页面
        """
        try:
            self.OrderManagermentBusiness()
            self.assertTrue(self.c.verify_modify_function())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('OrderTest_004_details_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img("OrderTest_005_reset_fail")
    def test_005_Verify_Reset(self):
        """
        用例五 ：验证重置功能
        """
        try:  # 传参,先输入门店名称,点击重置
            sleep(2)
            self.OrderManagermentBusiness()
            self.assertIn('', self.c.verify_reset_function(shop_name))  # 重置成功则返回''
        except (BaseException, AssertionError) as msg:
            self.c.save_img('OrderTest_005_reset_fail')
            InsertLog().debug(msg)
            raise BaseException

if __name__ == '__main__':
    unittest.main(verbosity=2)