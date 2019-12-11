from time import sleep
import unittest
from libs.ShareBusiness import login_C
from libs.ShareModules import InsertLog
from BeautifulReport import BeautifulReport
from PO.Pagetitle import PageTitle
from PO.BasePage import Base
from PO.ShopPage.ShopList import Shop
from libs.ShareModules import Getdata
'''读取测试数据'''
shop_name = Getdata('ShopList_tc', 'shop_name')
tel = Getdata('ShopList_tc', 'tel')
shop_number = Getdata('ShopList_tc', 'shop_number')
add_shop_name = Base.create_string(5)

class ShopListTest(unittest.TestCase):
    """测试 门店--门店列表 页面"""

    @classmethod
    def setUpClass(self):
        self.a = login_C()
        self.b = PageTitle(self.a)
        self.c = Shop(self.a)

    @classmethod
    def tearDownClass(self):
        self.c.close_broser()

    def ShopListBusiness(self):
        self.b.switch_to_OrderPage()
        sleep(1)
        self.b.switch_to_ShopPage()
        sleep(1)
        self.c.click_shop_list()

    @BeautifulReport.add_img('001_page_error')
    def test_001_Check_page(self):
        """
        用例一 ：检查页面是否正常
        """
        try:
            self.ShopListBusiness()
            self.assertTrue(self.c.get_newshop_msg())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('001_page_error')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('002_add_shop_fail')
    def test_002_Add_Shop(self):
        """
        用例二 ：新增门店
        """
        try:  # 传参 门店名称,门店地址,门店电话
            self.ShopListBusiness()
            self.assertTrue(self.c.add_shop_success(add_shop_name, u'深圳南山', tel))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('002_add_shop_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('003_search_fail')
    def test_003_Verify_Shop_number(self):
        """
        用例三 ：验证门店编号查询
        """
        try:  # 传参 需要查询的门店编号
            sleep(1)
            self.ShopListBusiness()
            self.assertTrue(self.c.verify_shop_number_query(shop_number))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('003_search_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('004_search_fail')
    def test_004_Verify_Shop_Name(self):
        """
        用例四 ：验证门店名称查询
        """
        try:  # 传参 需要查询的门店名称
            self.ShopListBusiness()
            self.assertTrue(self.c.verify_shop_name_query(shop_name))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('004_search_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('005_search_fail')
    def test_005_Verify_Tel_Phone(self):
        """
        用例五 ：验证电话查询
        """
        try:  # 传参 需要查询的电话
            self.ShopListBusiness()
            self.assertTrue(self.c.verify_telephone_query(tel))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('005_search_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('006_reset_fail')
    def test_006_Verify_Reset(self):
        """
        用例六 ：验证重置功能
        """
        try:  # 传参任意,先输入门店名称,点击重置
            test = u'门店'
            self.ShopListBusiness()
            self.assertIn('', self.c.verify_reset_function(test))  # 重置成功则返回''
        except (BaseException, AssertionError) as msg:
            self.c.save_img('006_reset_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('007_edit_fail')
    def test_007_Verify_Edit_Success(self):
        """
        用例七 ：验证编辑成功后返回信息
        """
        try:
            sleep(1)
            self.ShopListBusiness()
            self.assertTrue(self.c.verify_edit_function())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('007_edit_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('008_delete_fail')
    def test_008_Verify_Delete_Success(self):
        """
        用例八 ：验证删除成功后返回信息
        """
        try:
            self.ShopListBusiness()
            self.assertTrue(self.c.verify_delete_function())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('008_delete_fail')
            InsertLog().debug(msg)
            raise BaseException


if __name__ == '__main__':
    unittest.main(verbosity=2)