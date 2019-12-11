from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from PO.Page import Page
from PO.BasePage import Base

class Shop(Page, Base):
    """门店--门店列表 页面"""

    # 对象层
    ck_shop_loc = (By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/aside/ul/li')  # 门店列表
    txt_add_store_loc = (By.XPATH, '//*[@class="headbox commonToolbox"]/button/span/span[1]')  # 点击新增门店
    ipt_shop_number_loc = (By.CSS_SELECTOR, 'input[placeholder="Store number"]')   # 门店编号
    ipt_shop_name_loc = (By.CSS_SELECTOR, 'input[placeholder="Store name"]')  # 门店名称
    ipt_telphone_loc = (By.CSS_SELECTOR, 'input[placeholder="Phone no."]')  # 电话

    ck_search_loc = (By.XPATH, "//span[.='Search']")  # 点击查询
    ck_reset_loc = (By.XPATH, "//span[.='Reset']")  # 点击重置
    ck_edit_shop_loc = (By.XPATH, "//span[.='Edit']")  # 点击编辑
    ck_delete_loc = (By.XPATH, "//span[.='Delete']")  # 点击删除
    ck_confirm_delete_loc = (By.XPATH, '/html/body/div[2]/div/div[3]/button[2]/span')
    txt_datele_msg = (By.XPATH, '/html/body/div[3]/p')  # 获取删除返回的提示信息
    ck_save_loc = (By.XPATH, "//span[.='Save']")  # 点击保存
    txt_save_msg = (By.XPATH, '/html/body/div[2]/p')  # 获取保存返回的提示信息/html/body/div[4]/p

    txt_shop_number_msg = (By.XPATH, '//*[@class="el-table__row commonTableRow"]/td[2]/div')
    txt_shop_name_msg = (By.XPATH, '//*[@class="el-table__row commonTableRow"]/td[3]/div')
    txt_telephone_msg = (By.XPATH, '//*[@class="el-table__row commonTableRow"]/td[5]/div')

    """新增门店"""
    ipt_name_loc = (By.CSS_SELECTOR, 'input[placeholder="Please enter store name"]')  # 门店名称
    ipt_adderss_loc = (By.CSS_SELECTOR, 'input[placeholder="Store address cannot be empty"]')  # 门店地址
    ipt_phone_loc = (By.CSS_SELECTOR, 'input[placeholder="Please enter store phone number"]')  # 门店编号
    ck_fee_loc = (By.CSS_SELECTOR, 'input[placeholder="Please select a fee"]')  # 选择门店费用
    st_fee_loc = (By.XPATH, '//*[@class="el-select-dropdown el-popper"]/div[1]/div[1]/ul/li')  # 选择第一个门店费用
    ck_add_loc = (By.XPATH, "//span[.='Add']")  # 保存
    txt_save1_msg = (By.XPATH, '/html/body/div[4]/p')  # 获取保存返回的提示信息

    # 操作层
    def click_shop_list(self):
        """点击 门店列表"""
        self.driver.find_element(*self.ck_shop_loc).click()

    def get_newshop_msg(self):
        """获取新增门店文本"""
        WebDriverWait(self.driver, 5, 0.5).until(
            EC.text_to_be_present_in_element(self.txt_add_store_loc, u"New store"))
        r = self.driver.find_element(*self.txt_add_store_loc).text
        return r

    def add_shop_success(self, text, text1, text2):
        """新增门店流程"""
        self.driver.find_element(*self.txt_add_store_loc).click()
        self.driver.find_element(*self.ipt_name_loc).send_keys(text)     # 输入门店名称
        self.driver.find_element(*self.ipt_adderss_loc).send_keys(text1)  # 输入门店地址
        self.driver.find_element(*self.ipt_phone_loc).send_keys(text2)   # 输入门店电话
        self.driver.find_element(*self.ck_fee_loc).click()   # 选择消费税
        sleep(1)
        self.driver.find_element(*self.st_fee_loc).click()  # 选择服务税
        self.driver.find_element(*self.ck_add_loc).click()
        # WebDriverWait(self.driver, 5, 0.5).until(
        #     EC.text_to_be_present_in_element(self.txt_save_msg, u"New store successfully added"))
        # r = self.driver.find_element(*self.txt_save_msg).text
        # print(r)
        return True

    def verify_shop_number_query(self, text):
        """验证 门店编号 查询"""
        self.driver.find_element(*self.ipt_shop_number_loc).send_keys(text)
        self.driver.find_element(*self.ck_search_loc).click()
        WebDriverWait(self.driver, 5, 0.5).until(
            EC.text_to_be_present_in_element(self.txt_shop_number_msg, u'%s'% text))
        r = self.driver.find_element(*self.txt_shop_number_msg).text
        return r

    def verify_shop_name_query(self, text):
        """验证 门店名称 查询"""
        self.driver.find_element(*self.ipt_shop_name_loc).send_keys(text)
        self.driver.find_element(*self.ck_search_loc).click()
        WebDriverWait(self.driver, 5, 0.5).until(
            EC.text_to_be_present_in_element(self.txt_shop_name_msg, u'%s'% text))
        r = self.driver.find_element(*self.txt_shop_name_msg).text
        return r

    def verify_telephone_query(self, text):
        """验证 电话 查询"""
        self.driver.find_element(*self.ipt_telphone_loc).send_keys(text)
        self.driver.find_element(*self.ck_search_loc).click()
        WebDriverWait(self.driver, 5, 0.5).until(
            EC.text_to_be_present_in_element(self.txt_telephone_msg, u'%s'% text))
        r = self.driver.find_element(*self.txt_telephone_msg).text
        return r

    def verify_edit_function(self):
        """验证 编辑功能"""
        self.driver.find_element(*self.ck_edit_shop_loc).click()
        sleep(1)
        self.driver.find_element(*self.ck_save_loc).click()
        WebDriverWait(self.driver, 5, 0.5).until(
            EC.text_to_be_present_in_element(self.txt_save_msg, u'Store details edited successfully'))
        sleep(1)
        r = self.driver.find_element(*self.txt_save_msg).text
        self.driver.refresh()
        return r

    def verify_delete_function(self):
        """验证 删除功能"""
        self.driver.find_element(*self.ck_delete_loc).click()
        sleep(1)
        a = self.driver.find_element(*self.ck_confirm_delete_loc)
        action_a = ActionChains(self.driver)
        action_a.move_to_element(a).click().perform()
        WebDriverWait(self.driver, 5, 0.5).until(
            EC.text_to_be_present_in_element(self.txt_datele_msg, u'Successfully deleted'))
        sleep(1)
        r = self.driver.find_element(*self.txt_datele_msg).text
        self.driver.refresh()
        return r

    def verify_reset_function(self, text):
        """验证 重置功能"""
        self.driver.find_element(*self.ipt_shop_name_loc).send_keys(text)
        self.driver.find_element(*self.ck_reset_loc).click()
        r = self.driver.find_element(*self.ipt_shop_name_loc).text
        return r