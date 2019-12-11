# -*- coding: utf-8 -*-
# @file: G_ReportCurrencyList_tc.py
from time import sleep
import unittest
from libs.ShareBusiness import login_B
from libs.ShareModules import InsertLog
from libs.ShareModules import Screenshot
from po.Pagetitle import PageTitle
from po.ReportFormPage.DigitalCurrencyRecordList import DigitalCurrencyRecord
from libs.ShareModules import Getdata
'''读取测试数据'''
shop_name = Getdata('OrderManagementList_tc','shop_name')
start_day = Getdata('AssetsSalesList_tc','start_day')
end_day = Getdata('AssetsSalesList_tc','end_day')
trading_number = Getdata('ReportDigitalCurrencyRecordList_tc','trading_number')
order_number = Getdata('ReportDigitalCurrencyRecordList_tc','order_number')

class DigitalCurrencyRecordListTest(unittest.TestCase):
    '''报表--数字货币记录 页面'''
    @classmethod
    def setUpClass(self):
        self.a = login_B()
        self.b = PageTitle(self.a)
        self.c = DigitalCurrencyRecord(self.a)

    @classmethod
    def tearDownClass(self):
        sleep(40)  # 防止提示验证码发送过快
        self.c.close_broser()

    def DigitalCurrencyRecordList(self):
        self.b.switch_to_HomePage()
        sleep(1)
        self.b.switch_to_ReportFormPage()
        sleep(1)
        self.c.click_DigitalCurrencyRecordList()

    def test_001_Check_page(self):
        '''
        用例一 ：检查页面是否正常
        '''
        try:
            self.DigitalCurrencyRecordList()
            msg = self.c.get_Digital_record_msg_txt()
            self.assertEqual(msg,u'数字货币记录')
        except (BaseException,AssertionError) as msg:  # BaseException所有异常的基类,AssertionError断言语句失败
            Screenshot(self.a)
            InsertLog().debug(msg)
            raise BaseException

    def test_002_Verify_Input_Shop_Name(self):
        '''
        用例二 ：验证门店名称使用输入的方式查询
        '''
        try: # 传参 需要查询的门店名称
            self.DigitalCurrencyRecordList()
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
            self.DigitalCurrencyRecordList()
            msg = self.c.verify_select_shop_query()
            self.assertTrue(msg)  # 验证查询结果中的门店信息是否包含'门店'文本信息
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
            self.DigitalCurrencyRecordList()
            msg = self.c.verify_reset_function(shop_name)
            self.assertEqual(msg,"") # 重置成功则返回为空字符串
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
            self.DigitalCurrencyRecordList()
            msg = self.c.verify_day_query(start_day,end_day)
            self.assertTrue(msg)
            print('日期查询结果,返回信息：%s' % msg)
        except (BaseException, AssertionError) as msg:
            Screenshot(self.a)
            InsertLog().debug(msg)
            raise BaseException

    def test_006_Verify_Trading_Number(self):
        '''
        用例六 ：验证交易流水号查询功能
        '''
        try: # 传参 交易流水号
            self.DigitalCurrencyRecordList()
            msg = self.c.verify_trading_number(trading_number)
            self.assertEqual(msg,trading_number)
            print('交易流水号查询结果,返回信息：%s' % msg)
        except (BaseException, AssertionError) as msg:
            Screenshot(self.a)
            InsertLog().debug(msg)
            raise BaseException

    def test_007_Verify_Day_Query(self):
        '''
        用例七 ：验证订单号查询功能
        '''
        try: # 传参 订单号
            self.DigitalCurrencyRecordList()
            msg = self.c.verify_order_number(order_number)
            self.assertEqual(msg,order_number)
            print('订单号查询结果,返回信息：%s' % msg)
        except (BaseException, AssertionError) as msg:
            Screenshot(self.a)
            InsertLog().debug(msg)
            raise BaseException

    def test_008_Verify_Cashier(self):
        '''
        用例七 ：验证收银员查询功能
        '''
        try:
            self.DigitalCurrencyRecordList()
            msg = self.c.verify_cashier()
            self.assertTrue(msg)
            print('收银员查询,返回信息：%s' % msg)
        except (BaseException, AssertionError) as msg:
            Screenshot(self.a)
            InsertLog().debug(msg)
            raise BaseException

if __name__ == '__main__':
    unittest.main(verbosity=2)