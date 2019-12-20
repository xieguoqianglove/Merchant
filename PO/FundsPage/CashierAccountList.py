from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PO.Page import Page
from PO.BasePage import Base

class CashierAccount(Page, Base):
    """资产--收银账户 页面"""

    # 对象层
    ck_cashier_loc = (By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/aside/ul/li[1]')  # 现金收银
    txt_account_history_loc = (By.XPATH, '//span[.="Account history"]')  # 财务记录

    '''提现DAI、提现USDT'''
    ck_withdrawal_DAI_loc = (By.XPATH, '//*[@class="el-table__body-wrapper is-scrolling-none"]/table/tbody/tr[1]/td[5]/div/button/span')  # 点击Dai提现
    ck_withdrawal_USDT_loc = (By.XPATH, '//*[@class="el-table__body-wrapper is-scrolling-none"]/table/tbody/tr[2]/td[5]/div/button/span')  # 点击USDT提现
    ipt_address_loc = (By.XPATH, '//*[@id="addressForm"]/div[2]/div/div/div[1]/input')  # 输入地址
    ipt_volume_loc = (By.XPATH, '//*[@id="addressForm"]/div[3]/div/div/div/input')  # 输入数量
    ipt_paypwd_loc = (By.XPATH, '//*[@id="addressForm"]/div[5]/div/div/div[1]/input')  # 支付密码
    ck_sms_send_loc = (By.XPATH, '//*[@id="addressForm"]/div[6]/button')  # 点击获取手机验证码
    ipt_sms_code = (By.XPATH, '//*[@id="addressForm"]/div[6]/div/div/div[1]/input')  # 输入手机验证码
    ck_email_send_loc = (By.XPATH, '//*[@id="addressForm"]/div[7]/button')  # 点击获取邮箱验证码
    ipt_email_code = (By.XPATH, '//*[@id="addressForm"]/div[7]/div/div/div[1]/input')  # 输入邮箱验证码
    ck_submit_loc = (By.XPATH, '//span[.="Submit"]')  # 提交提现信息
    get_error_msg = (By.CSS_SELECTOR, 'p.el-message__content')  # 提示语

    '''财务记录菜单'''
    ck_Received_loc = (By.XPATH, '//*[@class="toolbar"]/div/label[2]/span')
    txt_received_msg = (By.XPATH, '//*[@class="el-table__row commonTableRow"]/td[3]/div/span')
    ck_Refund_loc = (By.XPATH, '//*[@class="toolbar"]/div/label[3]/span')
    ck_Withdrawal_loc = (By.XPATH, '//*[@class="toolbar"]/div/label[4]/span')
    txt_msg = (By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/div[3]/div/div[3]/div/span')

    # 操作层
    def click_cashier_account(self):
        """点击 收银账户"""
        self.driver.find_element(*self.ck_cashier_loc).click()

    def get_account_history_txt(self):
        """获取财务记录文本"""
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.txt_account_history_loc, "Account history"))
        return self.driver.find_element(*self.txt_account_history_loc).text

    def withdrawal_info(self, text, text1):
        """提现信息"""
        self.driver.find_element(*self.ipt_address_loc).send_keys(text)
        self.driver.find_element(*self.ipt_volume_loc).send_keys('1')
        self.driver.find_element(*self.ipt_paypwd_loc).send_keys(text1)
        self.driver.find_element(*self.ck_sms_send_loc).click()
        sleep(5)
        self.driver.find_element(*self.ipt_sms_code).send_keys('2222')
        self.driver.find_element(*self.ck_email_send_loc).click()
        sleep(5)
        self.driver.find_element(*self.ipt_email_code).send_keys('2222')
        self.driver.find_element(*self.ck_submit_loc).click()
        WebDriverWait(self.driver, 5, 0.5).until(
            EC.text_to_be_present_in_element(self.get_error_msg, 'Withdrawal submitted successfully' or
                                             '50000 Funds is empty' or
                                             '20010 The SMS verification code is incorrect' or
                                             '40007 Wrong password' or
                                             '20013 The Email verification code is incorrect'))
        return self.driver.find_element(*self.get_error_msg).text

    def withdrawal_DAI(self, text, text1):
        """提现DAI"""
        Dai_xpath = (By.XPATH, '//span[starts-with(., "DAI")]')
        self.driver.find_element(*Dai_xpath).click()
        sleep(1)
        return self.withdrawal_info(text, text1)

    def withdrawal_USDT(self, text, text1):
        """提现USDT"""
        USDT_xpath = (By.XPATH, '//span[starts-with(., "USDT")]')
        self.driver.find_element(*USDT_xpath).click()
        sleep(1)
        return self.withdrawal_info(text, text1)

    def click_receivables(self):
        """点击财务记录-收款"""
        self.driver.find_element(*self.txt_account_history_loc).click()
        sleep(1)
        self.driver.find_element(*self.ck_Received_loc).click()
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.txt_received_msg, "Received"))
        return self.driver.find_element(*self.txt_received_msg).text

    def click_refund(self):
        """点击财务记录-退款"""
        self.driver.find_element(*self.txt_account_history_loc).click()
        sleep(1)
        self.driver.find_element(*self.ck_Refund_loc).click()
        if self.findElement('No data'):
            return True

    def click_withdrawal(self):
        """点击财务记录-提现"""
        self.driver.find_element(*self.txt_account_history_loc).click()
        sleep(1)
        self.driver.find_element(*self.ck_Withdrawal_loc).click()
        if self.findElement('No data'):
            return True

