from selenium.webdriver.common.by import By
from time import sleep
from PO.Page import Page
from PO.BasePage import Base

class OrderManagement(Page, Base):
    """订单--订单管理 页面"""

    # 对象层
    ck_order_loc = (By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/aside/ul/li')  # 点击订单管理
    ck_shop_loc =(By.CSS_SELECTOR, "span.el-input__suffix")  # 点击shop
    ipt_shop_loc =(By.CSS_SELECTOR, "input[placeholder='Please enter content']")  # 输入门店名称
    ck_one_shop_loc =(By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section/main/form/div/div[1]/div/div[2]/div[2]/div/label/span[2]')  # 点击第一个门店名称
    ck_all_shop_loc =(By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section/main/form/div/div[1]/div/div[2]/div[2]/label/span[2]')  # 点击选择全部
    txt_shop_msg =(By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section/main/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[4]/div')  # 获取门店名称文本
    ck_search_loc = (By.XPATH, "//span[.='Search']")   # 点击查询
    ck_reset_loc = (By.XPATH, "//span[.='Reset']")  # 点击重置
    ck_details_loc =(By.XPATH, "//span[.='Details']")   # 点击详情
    txt_collection_info_loc =(By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section/main/div[3]/div/div[2]/div/div[1]/h3')   # 获取详情页面信息

    # 操作层
    def click_OrderManagement(self):
        """点击 订单管理"""
        self.driver.find_element(*self.ck_order_loc).click()

    def input_shop_query(self, text):
        """验证 输入方式的门店 查询"""
        self.driver.find_element(*self.ck_shop_loc).click()
        self.driver.find_element(*self.ipt_shop_loc).send_keys(text)
        sleep(1)
        self.driver.find_element(*self.ck_one_shop_loc).click()
        self.driver.find_element(*self.ck_search_loc).click()
        sleep(1)
        r = self.driver.find_element(*self.txt_shop_msg).text
        return r

    def verify_select_shop_query(self):
        """验证 选择方式的门店 查询 """
        self.driver.find_element(*self.ck_shop_loc).click()
        self.driver.find_element(*self.ck_all_shop_loc).click()
        sleep(1)
        self.driver.find_element(*self.ck_search_loc).click()
        sleep(1)
        r = self.driver.find_element(*self.txt_shop_msg).text
        return r

    def verify_modify_function(self):
        """验证 详情功能"""
        self.driver.find_element(*self.ck_details_loc).click()
        sleep(1)
        r = self.driver.find_element(*self.txt_collection_info_loc).text
        self.driver.refresh()  # 刷新页面
        return r

    def verify_reset_function(self, text):
        """验证 重置功能"""
        self.driver.find_element(*self.ck_shop_loc).click()
        self.driver.find_element(*self.ipt_shop_loc).send_keys(text)
        sleep(1)
        self.driver.find_element(*self.ck_one_shop_loc).click()
        self.driver.find_element(*self.ck_search_loc).click()
        sleep(1)
        self.driver.find_element(*self.ck_reset_loc).click()
        r = self.driver.find_element(*self.ipt_shop_loc).text
        return r
