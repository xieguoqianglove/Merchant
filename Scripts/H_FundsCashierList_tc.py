from time import sleep
import unittest
from libs.ShareBusiness import login_C
from libs.ShareModules import Getdata
from libs.ShareModules import InsertLog
from PO.Pagetitle import PageTitle
from PO.FundsPage.CashierAccountList import CashierAccount
from BeautifulReport import BeautifulReport
'''读取测试数据'''
withdrawal_address = Getdata('Funds_tc', 'withdrawal_address')
paypwd = Getdata('Funds_tc', 'paypwd')

class AssetsCashierListTest(unittest.TestCase):
    """测试 资产 菜单-- 收银账户 页面"""

    @classmethod
    def setUpClass(self):
        self.a = login_C()
        self.b = PageTitle(self.a)
        self.c = CashierAccount(self.a)

    @classmethod
    def tearDownClass(self):
        self.c.close_broser()

    def CashierAccounListBusiness(self):
        self.b.switch_to_OrderPage()
        sleep(1)
        self.b.switch_to_AssetsPage()
        sleep(1)
        self.c.click_cashier_account()

    @BeautifulReport.add_img('AssetsCash_001_funds_cashier_account_fail')
    def test_001_Cashier_Account_page(self):
        """
        用例一 ：检查页面是否正常
        """
        try:
            self.CashierAccounListBusiness()
            self.assertTrue(self.c.get_account_history_txt())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('AssetsCash_001_funds_cashier_account_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('AssetsCash_002_funds_withdrawal_usdt_fail')
    def test_002_Withdrawal_USDT(self):
        """
        用例二 ：提现USDT功能
        """
        try:  # 传参提现地址,支付密码
            self.CashierAccounListBusiness()
            self.assertTrue(self.c.withdrawal_USDT(withdrawal_address, paypwd))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('AssetsCash_002_funds_withdrawal_usdt_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('AssetsCash_003_funds_withdrawal_dai_fail')
    def test_003_Withdrawal_DAI(self):
        """
        用例三 ：提现DAI功能
        """
        try:  # 传参提现地址,支付密码
            self.CashierAccounListBusiness()
            self.assertTrue(self.c.withdrawal_DAI(withdrawal_address, paypwd))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('AssetsCash_003_funds_withdrawal_dai_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('AssetsCash_004_funds_withdrawal_received_fail')
    def test_004_Click_Receivables(self):
        """
        用例四 ：检查财务记录-收款页面
        """
        try:
            self.CashierAccounListBusiness()
            self.assertTrue(self.c.click_receivables())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('AssetsCash_004_funds_withdrawal_received_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('AssetsCash_005_funds_withdrawal_fail')
    def test_005_Click_Withdrawal(self):
        """
        用例五 ：检查财务记录-提现页面
        """
        try:
            self.CashierAccounListBusiness()
            self.assertTrue(self.c.click_withdrawal())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('AssetsCash_005_funds_withdrawal_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('AssetsCash_006_funds_withdrawal_refund_fail')
    def test_006_Click_Refund(self):
        """
        用例六 ：检查财务记录-退款页面
        """
        try:
            self.CashierAccounListBusiness()
            self.assertTrue(self.c.click_refund())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('AssetsCash_006_funds_withdrawal_refund_fail')
            InsertLog().debug(msg)
            raise BaseException

if __name__ == '__main__':
    unittest.main(verbosity=2)