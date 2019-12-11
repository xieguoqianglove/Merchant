from time import sleep
import unittest
from libs.ShareBusiness import login_C
from libs.ShareModules import InsertLog
from PO.Pagetitle import PageTitle
from BeautifulReport import BeautifulReport
from PO.ReportFormPage.OverviewAndCashList import OverviewAndCash
from libs.ShareModules import Getdata
'''读取测试数据'''
shop_name = Getdata('OrderManagementList_tc', 'shop_name')
start_day = Getdata('AssetsSalesList_tc', 'start_day')
end_day = Getdata('AssetsSalesList_tc', 'end_day')

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
        self.c.click_CashRecordList()

    @BeautifulReport.add_img("001_page_fail")
    def test_001_Check_page(self):
        """
        用例一 ：检查概览页面是否正常
        """
        try:
            self.b.switch_to_ReportFormPage()
            sleep(1)
            self.c.click_OverviewList()
            self.assertTrue(self.c.get_Cash_msg_txt())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('001_page_fail')
            InsertLog().debug(msg)
            raise BaseException

    def test_001_Check_page(self):
        '''
        用例一 ：检查页面是否正常
        '''
        try:
            self.CashRecordListBusiness()
            msg = self.c.get_carh_msg_txt()
            self.assertEqual(msg,u'现金记录')
        except (BaseException,AssertionError) as msg:  # BaseException所有异常的基类,AssertionError断言语句失败
            Screenshot(self.a)
            InsertLog().debug(msg)
            raise BaseException

    def test_002_Verify_Input_Shop_Name(self):
        '''
        用例二 ：验证门店名称使用输入的方式查询
        '''
        try: # 传参 需要查询的门店名称
            self.CashRecordListBusiness()
            sleep(1)
            msg = self.c.verify_input_shop_query(shop_name)
            self.assertEqual(msg,shop_name)
            print('门店名称使用输入的方式查询,页面返回值：%s' % msg)
        except (BaseException, AssertionError) as msg:
            Screenshot(self.a)
            InsertLog().debug(msg)
            raise BaseException

    def test_003_Verify_Select_Shop_name(self):
        '''
        用例三 ：验证门店名称使用全选的方式查询
        '''
        try:
            self.CashRecordListBusiness()
            msg = self.c.verify_select_shop_query()
            self.assertTrue(msg)
            print('门店名称使用全选的方式查询,页面返回值：%s' % msg)
        except (BaseException, AssertionError) as msg:
            Screenshot(self.a)
            InsertLog().debug(msg)
            raise BaseException

    def test_004_Verify_Reset(self):
        '''
        用例四 ：验证重置功能
        '''
        try: # 传参,先输入门店名称,点击重置
            self.CashRecordListBusiness()
            msg = self.c.verify_reset_function(shop_name)
            self.assertEqual(msg,'') # 重置成功则返回空字符串
            print('重置成功,返回信息：%s' % msg)
        except (BaseException, AssertionError) as msg:
            Screenshot(self.a)
            InsertLog().debug(msg)
            raise BaseException

    def test_005_Verify_Day_Query(self):
        '''
        用例五 ：验证日期查询功能
        '''
        try: # 传参 开始日期和结束日期,只能输入比当前日期前一天的时间
            self.CashRecordListBusiness()
            msg = self.c.verify_day_query(start_day,end_day)
            self.assertTrue(msg)
            print('日期查询结果,返回信息：%s' % msg)
        except (BaseException, AssertionError) as msg:
            Screenshot(self.a)
            InsertLog().debug(msg)
            raise BaseException

if __name__ == '__main__':
    unittest.main(verbosity=2)