from time import sleep
import unittest
from libs.ShareBusiness import login_C
from libs.ShareModules import InsertLog
from libs.ShareModules import Getdata
from PO.Pagetitle import PageTitle
from PO.FundsPage.SalesAccountList import SalesAccount
from BeautifulReport import BeautifulReport
'''读取测试数据'''
withdrawal_address = Getdata('Funds_tc', 'withdrawal_address')
paypwd = Getdata('Funds_tc', 'paypwd')
start_day = Getdata('ReportCashList_tc', 'start_day')
end_day = Getdata('ReportCashList_tc', 'end_day')

class AssetsSalesListTest(unittest.TestCase):
    """测试 资产 菜单-- 销售账户 页面"""

    @classmethod
    def setUpClass(self):
        self.a = login_C()
        self.b = PageTitle(self.a)
        self.c = SalesAccount(self.a)

    @classmethod
    def tearDownClass(self):
        self.c.close_broser()

    def AssetsListBusiness(self):
        self.b.switch_to_OrderPage()
        sleep(1)
        self.b.switch_to_AssetsPage()
        sleep(1)
        self.c.click_sales_account()

    @BeautifulReport.add_img('001_funds_sales_account_fail')
    def test_001_Cashier_Account_page(self):
        """
        用例一 ：检查页面是否正常
        """
        try:
            self.AssetsListBusiness()
            self.assertTrue(self.c.get_account_history_txt())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('001_funds_sales_account_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('002_funds_withdrawal_usdt_fail')
    def test_002_Withdrawal_USDT(self):
        """
        用例二 ：提现USDT功能
        """
        try:  # 传参提现地址,支付密码
            self.AssetsListBusiness()
            self.assertTrue(self.c.withdrawal_USDT(withdrawal_address, paypwd))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('002_funds_withdrawal_usdt_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('003_funds_withdrawal_dai_fail')
    def test_003_Withdrawal_DAI(self):
        """
        用例三 ：提现DAI功能
        """
        try:  # 传参提现地址,支付密码
            self.AssetsListBusiness()
            self.assertTrue(self.c.withdrawal_DAI(withdrawal_address, paypwd))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('003_funds_withdrawal_dai_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('004_deposit_fail')
    def test_004_Deposit_Function(self):
        """
        用例四 ：检验充值功能
        """
        try:
            self.AssetsListBusiness()
            self.assertTrue(self.c.click_deposit())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('004_deposit_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('005_reset_fail')
    def test_005_Verify_Reset(self):
        """
        用例五 ：验证销售账户>重置功能
        """
        try:  # 传参,先输入开始日期,点击重置
            self.AssetsListBusiness()
            self.assertIn('', self.c.verify_reset_function(start_day))  # 重置成功则返回空字符串
        except (BaseException, AssertionError) as msg:
            self.c.save_img('005_reset_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('006_Day_fail')
    def test_006_Verify_Day_Query(self):
        """
        用例六 ：验证销售账户>日期查询功能
        """
        try:  # 传参 开始日期和结束日期,只能输入比当前日期前一天的时间
            self.AssetsListBusiness()
            self.assertIsNotNone(self.c.verify_day_query(start_day, end_day))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('006_Day_fail')
            InsertLog().debug(msg)
            raise BaseException


if __name__ == '__main__':
    unittest.main(verbosity=2)