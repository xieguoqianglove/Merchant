from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PO.Page import Page
from PO.BasePage import Base

class Setting(Page, Base):
    """设置--时区设置、费用管理"""

    # 对象层
    ck_setting_loc = (By.CSS_SELECTOR, 'div.iconBtn')  # 点击设置
    txt_time_zone_loc = (By.XPATH, '//*[@class="setting"]/section/aside/ul/li[1]/span')  # 获取时区的文本
    ck_time_setting_loc = (By.XPATH, '//*[@class="setting"]/section/aside/ul/li[1]/span')   # 设置时区
    ck_st_time_loc = (By.XPATH, '//*[@class="myRow commonFormRow"]/div/div/div/div[1]/input')
    ck_save_loc = (By.XPATH, "//span[.='Save']")  # 点击保存

    get_tips_msg = (By.CSS_SELECTOR, 'p.el-message__content')   # 提示语

    ck_fees_tax_loc = (By.XPATH, '//*[@class="setting"]/section/aside/ul/li[2]/span')   # 设置费用
    ck_add_fees_loc = (By.XPATH, '//span[.="Add a fee"]')  # 添加费用
    ck_fee_name_loc = (By.XPATH, '//*[@class="el-form el-form--label-top"]/div[1]/div/div/div[1]/input')  # 费用名称
    ck_cash_service_loc = (By.XPATH, '//*[@class="el-form el-form--label-top"]/div[2]/div/div/div[1]/input')  # 現金收款服務費
    ck_cash_tax_loc = (By.XPATH, '//*[@class="el-form el-form--label-top"]/div[3]/div/div/div[1]/input')  # 現金收款稅費
    ck_crypto_service_loc = (By.XPATH, '//*[@class="el-form el-form--label-top"]/div[4]/div/div/div[1]/input')   # 數字貨幣收款服務費稅
    ck_crypto_tax_loc = (By.XPATH, '//*[@class="el-form el-form--label-top"]/div[5]/div/div/div[1]/input')  # 數字貨幣收款稅費
    ck_submit_loc = (By.XPATH, "//span[.='Submit']")  # 点击提交
    ck_modify_loc = (By.XPATH, "//*[@class='el-table__row commonTableRow']/td[7]/div/button[1]/span")  # 点击修改
    ck_delete_loc = (By.XPATH, "//*[@class='el-table__row commonTableRow']/td[7]/div/button[2]/span")  # 点击删除
    ck_confirm_delete_loc = (By.XPATH, "//*[@class='el-message-box__btns']/button[2]")  # 点击确认删除

    ck_setting_crypto_loc = (By.XPATH, '//*[@class="setting"]/section/aside/ul/li[3]/span')  # 设置结算货币
    ck_crypto_loc = (By.CSS_SELECTOR, 'input[placeholder="Select a crypto"]')  # 设置结算货币


    def setting_crypto(self, crypto):
        """结算货币切换成DAI"""
        crypto_xpath = (By.XPATH, f'//span[starts-with(., "{crypto}")]')
        self.driver.find_element(*self.ck_setting_crypto_loc).click()
        sleep(0.5)
        self.driver.find_element(*self.ck_crypto_loc).click()
        sleep(0.5)
        self.driver.find_element(*crypto_xpath).click()
        sleep(0.5)
        self.driver.find_element(*self.ck_save_loc).click()
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.get_tips_msg, 'Successfully modified'))
        return self.driver.find_element(*self.get_tips_msg).text

    def click_setting(self):
        """进入设置界面"""
        WebDriverWait(self.driver, 10, 0.5).until(EC.text_to_be_present_in_element(self.txt_time_zone_loc, 'Time zone setting'))
        return self.driver.find_element(*self.txt_time_zone_loc).text

    def update_time_zone(self):
        """更新时区"""
        self.driver.find_element(*self.ck_time_setting_loc).click()
        self.driver.find_element(*self.ck_st_time_loc).click()
        sleep(0.5)
        time_xpath = (By.XPATH, f"//span[starts-with(.,'(GMT+09:00) Palau Time')]")  # 更新新时区
        self.driver.find_element(*time_xpath).click()
        sleep(1)
        self.driver.find_element(*self.ck_save_loc).click()
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.get_tips_msg, 'Successfully modified'))
        return self.driver.find_element(*self.get_tips_msg).text

    def add_fees_tax(self, text, text1, text2):
        """添加费用"""
        self.driver.find_element(*self.ck_fees_tax_loc).click()
        self.driver.find_element(*self.ck_add_fees_loc).click()
        sleep(1)
        self.driver.find_element(*self.ck_fee_name_loc).send_keys(text)
        self.driver.find_element(*self.ck_cash_service_loc).send_keys(text1)
        self.driver.find_element(*self.ck_cash_tax_loc).send_keys(text2)
        self.driver.find_element(*self.ck_crypto_service_loc).send_keys(text1)
        self.driver.find_element(*self.ck_crypto_tax_loc).send_keys(text2)
        self.driver.find_element(*self.ck_submit_loc).click()
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.get_tips_msg, 'Successfully added'))
        return self.driver.find_element(*self.get_tips_msg).text

    def update_fees_tax(self):
        """修改费用设置"""
        self.driver.find_element(*self.ck_fees_tax_loc).click()
        sleep(0.5)
        self.driver.find_element(*self.ck_modify_loc).click()
        sleep(0.5)
        self.driver.find_element(*self.ck_submit_loc).click()
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.get_tips_msg, 'Successfully modified'))
        return self.driver.find_element(*self.get_tips_msg).text

    def delete_fees_tax(self):
        """删除费用设置"""
        self.driver.find_element(*self.ck_fees_tax_loc).click()
        sleep(0.5)
        self.driver.find_element(*self.ck_delete_loc).click()
        sleep(1)
        self.driver.find_element(*self.ck_confirm_delete_loc).click()
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.get_tips_msg, 'Successfully deleted'))
        return self.driver.find_element(*self.get_tips_msg).text
