from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PO.Page import Page
from PO.BasePage import Base
from PO.FundsPage.CashierAccountList import CashierAccount

class SalesAccount(Page, Base):
    """资产--销售账户 页面"""

    # 对象层
    ck_sales_loc = (By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/aside/ul/li[2]')  # 销售账户
    txt_account_history_loc = (By.XPATH, '//span[.="Account history"]')  # 财务记录

    ck_deposit_loc = (By.XPATH, '//a[.="Deposit"]')  # 点击充值
    ck_button_recharge_loc = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span')
    txt_button_recharge_msg = (By.XPATH, '/html/body/div[3]/p')

    ck_withdrawal_loc = (By.XPATH, '//a[.="Withdrawal"]')  # 点击提现
    ck_crypto_loc = (By.CSS_SELECTOR, 'input[placeholder="Select a crypto"]')  # 选择提现币种
    '''提现DAI、提现USDT'''
    ck_withdrawal_DAI_loc = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[1]')  # 点击Dai提现
    ck_withdrawal_USDT_loc = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[2]')  # 点击USDT提现

    '''日期查询、查询、重置'''
    ipt_start_day_loc = (By.CSS_SELECTOR, 'input[placeholder="Start date"]')
    ipt_end_day_loc = (By.CSS_SELECTOR, 'input[placeholder="End date"]')
    ck_search_loc = (By.XPATH, "//span[.='Search']")  # 点击查询
    ck_reset_loc = (By.XPATH, "//span[.='Reset']")  # 点击重置
    txt_time_msg = (By.XPATH, '//*[@class="el-table__row commonTableRow"]/td[3]/div')

    # 操作层
    def click_sales_account(self):
        """点击 销售账户"""
        self.driver.find_element(*self.ck_sales_loc).click()

    def get_account_history_txt(self):
        """获取财务记录文本"""
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.txt_account_history_loc, "Account history"))
        return self.driver.find_element(*self.txt_account_history_loc).text

    def withdrawal_up(self):
        """提现入口"""
        self.driver.find_element(*self.ck_withdrawal_loc).click()
        sleep(1)
        self.driver.find_element(*self.ck_crypto_loc).click()
        sleep(1)

    def withdrawal_DAI(self, text, text1):
        """提现DAI"""
        self.withdrawal_up()
        self.driver.find_element(*self.ck_withdrawal_DAI_loc).click()
        sleep(1)
        CashierAccount.withdrawal_info(text, text1)

    def withdrawal_USDT(self, text, text1):
        """提现USDT"""
        self.withdrawal_up()
        self.driver.find_element(*self.ck_withdrawal_USDT_loc).click()
        sleep(1)
        CashierAccount.withdrawal_info(text, text1)

    def click_deposit(self):
        """点击充值 功能"""
        self.driver.find_element(*self.ck_deposit_loc).click()
        self.driver.find_element(*self.ck_button_recharge_loc).click()
        sleep(1)
        return self.driver.find_element(*self.txt_button_recharge_msg).text

    def verify_reset_function(self, text):
        """验证 重置功能"""
        self.driver.find_element(*self.txt_account_history_loc).click()
        sleep(1)
        self.driver.find_element(*self.ipt_start_day_loc).send_keys(text)
        self.driver.find_element(*self.ck_reset_loc).click()
        return self.driver.find_element(*self.ipt_start_day_loc).text

    def verify_day_query(self, text, text1):
        """验证 日期查询"""
        self.driver.find_element(*self.txt_account_history_loc).click()
        sleep(1)
        self.driver.find_element(*self.ipt_start_day_loc).send_keys(text)
        sleep(1)
        self.driver.find_element(*self.ipt_end_day_loc).send_keys(text1)
        self.driver.find_element(*self.ck_search_loc).click()
        sleep(1)
        return self.driver.find_element(*self.txt_time_msg).text