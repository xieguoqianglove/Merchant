from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PO.Page import Page
from PO.BasePage import Base

class Device(Page, Base):
    """设备——>设备列表"""

    # 对象层
    ck_dev_list_loc = (By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/aside/ul/li/span')  # 点击设备列表
    txt_dev_msg = (By.XPATH, '//*[@class="el-table__header-wrapper"]/table/thead/tr/th[2]/div')

    ipt_dev_Imei_loc = (By.CSS_SELECTOR, 'input[placeholder="Device IMEI"]')  # 输入imei
    ck_dev_status_loc = (By.CSS_SELECTOR, 'input[placeholder="Device status"]')   # 点击设备状态
    ck_store_loc = (By.CSS_SELECTOR, 'div.search-select')  # 点击门店
    ipt_store_name_loc = (By.CSS_SELECTOR, 'input[placeholder="Please enter content"]')  # 输入门店名称
    ck_one_shop_loc = (By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section/main/form/div/div[3]/div/div[2]/div[2]/div/label/span[2]')
    ck_normal_loc = (By.CSS_SELECTOR, '/html/body/div[4]/div[1]/div[1]/ul/li[2]/span')  # 选择normal

    txt_dev_imei_msg =(By.XPATH, '//*[@class="el-table__row commonTableRow"]/td[2]/div')
    txt_dev_status_msg =(By.XPATH, '//*[@class="el-table__row commonTableRow"]/td[8]/div')
    txt_dev_store_msg =(By.XPATH, '//*[@class="el-table__row commonTableRow"]/td[6]/div')

    ck_search_loc = (By.XPATH, "//span[.='Search']")  # 点击查询
    ck_reset_loc = (By.XPATH, "//span[.='Reset']")  # 点击重置
    ck_edit_loc = (By.XPATH, "//span[.='Edit']")  # 点击编辑

    ck_store_name = (By.CSS_SELECTOR, 'input[placeholder="Please select"]')  # 选择门店
    st_store_loc = (By.CSS_SELECTOR, '/html/body/div[4]/div[1]/div[1]/ul/li/span')  # 选择第一个门店
    ck_confirm_loc = (By.XPATH, '//span[.="Confirm"]')  # 点击确定
    txt_edit_success_msg =(By.XPATH, '/html/body/div[4]/p')  # 返回修改成功信息


    # 操作层
    def click_DeviceList(self):
        """点击 设备列表"""
        self.driver.find_element(*self.ck_dev_list_loc).click()

    def get_DeviceId_msg_txt(self):
        """获取设备id文本"""
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.txt_dev_msg, u"Device IMEI"))
        r = self.driver.find_element(*self.txt_dev_msg).text
        return r

    def verify_device_imei_query(self, text):
        """验证设备IMEI查询"""
        self.driver.find_element(*self.ipt_dev_Imei_loc).send_keys(text)
        self.driver.find_element(*self.ck_search_loc).click()
        sleep(1)
        r = self.driver.find_element(*self.txt_dev_imei_msg).text
        return r

    def verify_device_lock_status_query(self):
        """验证设备锁定状态查询"""
        self.driver.find_element(*self.ck_dev_status_loc).click()
        sleep(0.5)
        self.driver.find_element(*self.ck_normal_loc).click()
        self.driver.find_element(*self.ck_search_loc).click()
        sleep(1)
        r = self.driver.find_element(*self.txt_dev_status_msg).text
        return r

    def input_shop_query(self, text):
        """验证 输入方式的门店 查询"""
        self.driver.find_element(*self.ck_store_loc).click()
        self.driver.find_element(*self.ipt_store_name_loc).send_keys(text)
        sleep(1)
        self.driver.find_element(*self.ck_one_shop_loc).click()
        self.driver.find_element(*self.ck_search_loc).click()
        sleep(1)
        r = self.driver.find_element(*self.txt_dev_store_msg).text
        return r

    def verify_reset_function(self, text):
        """验证 重置功能"""
        self.driver.find_element(*self.ipt_dev_Imei_loc).send_keys(text)
        self.driver.find_element(*self.ck_reset_loc).click()
        r = self.driver.find_element(*self.ipt_dev_Imei_loc).text
        return r

    def verify_edit_success(self):
        """验证 编辑成功返回信息"""
        self.driver.find_element(*self.ck_edit_loc).click()
        sleep(1)
        self.driver.find_element(*self.ck_store_name).click()
        self.driver.find_element(*self.st_store_loc).click()
        self.driver.find_element(*self.ck_confirm_loc).click()
        WebDriverWait(self.driver, 5, 0.5).until(
            EC.text_to_be_present_in_element(self.txt_edit_success_msg, u'Successfully modified'))
        r = self.driver.find_element(*self.txt_edit_success_msg).text
        return r