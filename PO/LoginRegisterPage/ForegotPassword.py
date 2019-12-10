from time import sleep
from selenium.webdriver.common.by import By
from PO.Page import Page
from PO.BasePage import Base

class ForegotPasswordPage(Page, Base):
    """忘记密码页面"""

    # 对象层
    ipt_brand_number_loc =(By.CSS_SELECTOR, 'input[placeholder="Brand serial number"]')
    ck_nation_loc =(By.CSS_SELECTOR, 'input[placeholder="Country/Region"]')
    ipt_phone_number_loc = (By.CSS_SELECTOR, 'input[placeholder="Phone no."]')
    ck_send_phone_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/div/form/div[3]/div[2]/div/button')
    ipt_sms_code_loc = (By.CSS_SELECTOR, 'input[placeholder="Please enter verification code"]')
    ck_next_loc =(By.XPATH, '//*[@id="app"]/div/div[2]/div/form/button')
    ck_send_email_loc =(By.XPATH, '//*[@id="app"]/div/div[2]/div/div[2]/div/button')
    ipt_email_code_loc =(By.CSS_SELECTOR, 'input[placeholder="Please enter Email verification code"]')
    ck_next1_loc =(By.XPATH, '//*[@id="app"]/div/div[2]/div/button')

    ipt_new_password_loc = (By.CSS_SELECTOR, 'input[placeholder="Please enter login password"]')
    ipt_payment_pwd_loc = (By.CSS_SELECTOR, 'input[placeholder="Please confirm the login password"]')
    ck_complete_loc =(By.XPATH, '//*[@id="app"]/div/div[2]/div/form/button')
    txt_login_page_msg =(By.XPATH, '//*[@id="app"]/div/div[2]/div/form/button')

    # 操作层
    def input_brand_name(self, value):
        """输入品牌名称"""
        self.driver.find_element(*self.ipt_brand_number_loc).send_keys(value)

    def setect_nation(self, nation, phone):
        """选择国家"""
        self.driver.find_element(*self.ck_nation_loc).click()
        nation_xpath = (By.XPATH, f'//li[contains(., "{nation}")]')  # 定位国家
        self.driver.find_element(*nation_xpath).click()
        sleep(1)
        self.driver.find_element(*self.ipt_phone_number_loc).send_keys(phone)
        sleep(1)

    def input_code_and_next(self):
        """输入手机验证码、下一步"""
        self.driver.find_element(*self.ck_send_phone_loc).click()
        sleep(3)
        self.driver.find_element(*self.ipt_sms_code_loc).send_keys('2222')
        self.driver.find_element(*self.ck_next_loc).click()

    def input_eamil_code(self):
        """输入邮箱验证码、下一步"""
        self.driver.find_element(*self.ipt_email_code_loc).send_keys('2222')
        self.driver.find_element(*self.ck_next1_loc).click()

    def set_login_password(self, values):
        """输入新登录密码"""
        self.driver.find_element(*self.ipt_new_password_loc).send_keys(values)
        self.driver.find_element(*self.ipt_payment_pwd_loc).send_keys(values)
        self.driver.find_element(*self.ck_complete_loc).click()
        sleep(2)
        msg = self.driver.find_element(*self.txt_login_page_msg).text
        return msg