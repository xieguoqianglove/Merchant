from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PO.Page import Page
from PO.BasePage import Base
from time import sleep

class OverviewAndCash(Page, Base):
    """报表--概览\现金记录页面"""

    # 概览对象层
    ipt_overviewList_loc = (By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/aside/ul/li[1]')
    txt_cash_msg = (By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/div[2]/div[2]/div/label[1]/span[2]')

    # 操作层
    def click_OverviewList(self):
        """点击 概览"""
        self.driver.find_element(*self.ipt_overviewList_loc).click()

    def get_Cash_msg_txt(self):
        """获取 现金 文本"""
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.txt_cash_msg, u"Cash"))
        r = self.driver.find_element(*self.txt_cash_msg).text
        return r

    # 现金记录对象层
    ipt_carh_history_loc = (By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/aside/ul/li[2]')
    txt_carh_history_msg = (By.XPATH, '//*[@class="commonToolbox"]/h2')
    ipt_start_day_loc = (By.CSS_SELECTOR, 'input[placeholder="Start date"]')
    ipt_end_day_loc = (By.CSS_SELECTOR, 'input[placeholder="End date"]')

    ck_store_loc = (By.XPATH, "//span[.='Store']")  # 点击门店
    ipt_store_loc = (By.CSS_SELECTOR, 'input[placeholder="Please enter content"]')  # 输入门店名称
    st_one_store_loc = (By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section[2]/main/form/div/div[2]/div/div[2]/div[2]/div/label/span[1]')  # 输入门店名称
    st_all_store_loc = (By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section[2]/main/form/div/div[2]/div/div[2]/div[2]/label/span[1]')  # 输入门店名称
    ck_search_loc = (By.XPATH, "//span[.='Search']")  # 点击查询
    ck_reset_loc = (By.XPATH, "//span[.='Reset']")  # 点击重置

    txt_time_msg = (By.XPATH, '//*[@class="el-table__row commonTableRow"]/td[5]/div')
    txt_store_msg = (By.XPATH, '//*[@class="el-table__row commonTableRow"]/td[7]/div')


    def click_carh_history(self):
        """点击 现金记录"""
        self.driver.find_element(*self.ipt_carh_history_loc).click()

    def get_carh_history_txt(self):
        """获取  现金记录 文本"""
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.txt_carh_history_msg, u"Cash history"))
        r = self.driver.find_element(*self.txt_carh_history_msg).text
        return r

    def verify_input_shop_query(self, text):
        """验证 输入方式的门店 查询"""
        self.driver.find_element(*self.ck_store_loc).click()
        self.driver.find_element(*self.ipt_store_loc).send_keys(text)
        sleep(1)
        self.driver.find_element(*self.st_one_store_loc).click()
        self.driver.find_element(*self.ck_search_loc).click()
        WebDriverWait(self.driver, 5, 0.5).until(
            EC.text_to_be_present_in_element(self.txt_store_msg, u'%s' % text))
        r = self.driver.find_element(*self.txt_store_msg).text
        return r

    def verify_select_shop_query(self):
        """验证 选择方式的门店 查询"""
        self.driver.find_element(*self.ck_store_loc).click()
        self.driver.find_element(*self.st_all_store_loc).click()
        self.driver.find_element(*self.ck_search_loc).click()
        sleep(1)
        r = self.driver.find_element(*self.txt_store_msg).text
        return r

    def verify_reset_function(self, text):
        """验证 重置功能"""
        self.driver.find_element(*self.ipt_start_day_loc).send_keys(text)
        self.driver.find_element(*self.ck_reset_loc).click()
        r = self.driver.find_element(*self.ipt_start_day_loc).text
        return r

    def verify_day_query(self, text, text1):
        """验证 日期查询"""
        self.driver.find_element(*self.ipt_start_day_loc).send_keys(text)
        sleep(1)
        self.driver.find_element(*self.ipt_end_day_loc).send_keys(text1)
        self.driver.find_element(*self.ck_search_loc).click()
        sleep(1)
        r = self.driver.find_element(*self.txt_time_msg).text
        return r