from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PO.Page import Page
from PO.BasePage import Base

class DigitalCurrencyRecord(Page, Base):
    """报表--数字货币记录 页面"""

    # 对象层
    ipt_currency_history_loc = (By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/aside/ul/li[3]')
    txt_currency_history_msg = (By.XPATH, '//*[@class="commonToolbox"]/h2')
    ipt_start_day_loc = (By.CSS_SELECTOR, 'input[placeholder="Start date"]')
    ipt_end_day_loc = (By.CSS_SELECTOR, 'input[placeholder="End date"]')

    ck_store_loc = (By.XPATH, "//span[.='Store']")  # 点击门店
    ipt_store_loc = (By.CSS_SELECTOR, 'input[placeholder="Please enter content"]')  # 输入门店名称
    st_one_store_loc = (By.XPATH,
                        '//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section[2]/main/form/div/div[2]/div/div[2]/div[2]/div/label/span[1]')  # 输入门店名称
    st_all_store_loc = (By.XPATH,
                        '//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section[2]/main/form/div/div[2]/div/div[2]/div[2]/label/span[1]')  # 输入门店名称
    ipt_order_number_loc = (By.CSS_SELECTOR, 'input[placeholder="Order number"]')  # 输入订单编号
    ck_cash_name_loc = (By.CSS_SELECTOR, 'input[placeholder="Cashier name"]')  # 点击收银员
    st_cash_name_loc =(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[1]/span')  # 选择第一个人收银员
    ck_search_loc = (By.XPATH, "//span[.='Search']")  # 点击查询
    ck_reset_loc = (By.XPATH, "//span[.='Reset']")  # 点击重置
    txt_time_msg = (By.XPATH, '//*[@class="el-table__row commonTableRow"]/td[7]/div')
    txt_store_msg = (By.XPATH, '//*[@class="el-table__row commonTableRow"]/td[8]/div')
    txt_cash_name_msg = (By.XPATH, '//*[@class="el-table__row commonTableRow"]/td[6]/div')
    txt_order_number_msg = (By.XPATH, '//*[@class="el-table__row commonTableRow"]/td[1]/div')

    # 操作层
    def click_DigitalCurrencyRecordList(self):
        """点击 数字货币记录"""
        self.driver.find_element(*self.ipt_currency_history_loc).click()

    def get_Digital_record_msg_txt(self):
        """获取 数字货币记录 文本"""
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.txt_currency_history_msg, u"Cryptocurrency history"))
        return self.driver.find_element(*self.txt_currency_history_msg).text

    def verify_input_shop_query(self, text):
        """验证 输入方式的门店 查询"""
        shop_xpath = (By.XPATH, f'//span[contains(.,"{text}")]')
        self.driver.find_element(*self.ck_store_loc).click()
        self.driver.find_element(*self.ipt_store_loc).send_keys(text)
        sleep(0.5)
        self.driver.find_element(*shop_xpath).click()
        self.driver.find_element(*self.ck_search_loc).click()
        WebDriverWait(self.driver, 5, 0.5).until(
            EC.text_to_be_present_in_element(self.txt_store_msg, u'%s' % text))
        return self.driver.find_element(*self.txt_store_msg).text

    def verify_select_shop_query(self):
        """验证 选择方式的门店 查询"""
        self.driver.find_element(*self.ck_store_loc).click()
        self.driver.find_element(*self.st_all_store_loc).click()
        self.driver.find_element(*self.ck_search_loc).click()
        sleep(1)
        return self.driver.find_element(*self.txt_store_msg).text

    def verify_reset_function(self, text):
        """验证 重置功能"""
        self.driver.find_element(*self.ipt_start_day_loc).send_keys(text)
        self.driver.find_element(*self.ck_reset_loc).click()
        return self.driver.find_element(*self.ipt_start_day_loc).text

    def verify_day_query(self, text, text1):
        """验证 日期查询"""
        self.driver.find_element(*self.ipt_start_day_loc).send_keys(text)
        sleep(1)
        self.driver.find_element(*self.ipt_end_day_loc).send_keys(text1)
        self.driver.find_element(*self.ck_search_loc).click()
        sleep(1)
        return self.driver.find_element(*self.txt_time_msg).text

    def verify_order_number(self, text):
        """验证 订单号 查询"""
        self.driver.find_element(*self.ipt_order_number_loc).send_keys(text)
        self.driver.find_element(*self.ck_search_loc).click()
        return self.driver.find_element(*self.txt_order_number_msg).text

    def verify_cashier(self, cashier):
        """验证 收银员 查询,默认选择第一个"""
        cashier_xpath = (By.XPATH, f'//span[starts-with(.,"{cashier}")]')
        self.driver.find_element(*self.ck_cash_name_loc).click()
        sleep(0.5)
        self.driver.find_element(*cashier_xpath).click()
        return self.driver.find_element(*self.txt_cash_name_msg).text