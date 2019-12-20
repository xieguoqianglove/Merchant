from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PO.Page import Page
from PO.BasePage import Base

class RegisterPage(Page,Base):
    """商户后台注册页面"""

    # 对象层
    ck_free_registration_loc = (By.XPATH, '//*[@id="app"]/section/div[2]/div[1]/div[2]/p/a[1]')  # 注册
    ck_business_loc = (By.CSS_SELECTOR, 'input[placeholder="Please select business type"]')  # 点击类型
    st_business_loc = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[11]/span')  # 选择Gifts and flowers类型
    ipt_brand_name_loc = (By.CSS_SELECTOR, 'input[placeholder="Please enter brand name"]')  # 输入品牌名称
    ck_nation_loc = (By.CSS_SELECTOR, 'input[placeholder="Country/Region"]')  # 点击选择国家
    ipt_phone_number_loc = (By.CSS_SELECTOR, 'input[placeholder="Please enter phone number"]')   # 输入手机号码
    ck_sendsms_loc = (By.XPATH, '//*[@id="app"]/section/div[2]/div/form/div[2]/div[2]/div[2]/div/button')  # 发送验证码
    ipt_sms_code_loc = (By.CSS_SELECTOR, 'input[placeholder="Please enter verification code"]')  # 输入验证码
    ipt_pwd_loc = (By.CSS_SELECTOR, 'input[placeholder="Please enter login password"]')  # 输入登陆密码
    ipt_confirm_pwd_loc = (By.XPATH, '//*[@id="app"]/section/div[2]/div/form/div[3]/div[2]/div/div[1]/input')  # 输入登陆密码
    ipt_name_loc = (By.CSS_SELECTOR, 'input[placeholder="Enter first name"]')  # 输入名
    ipt_surname_loc = (By.CSS_SELECTOR, 'input[placeholder="Enter last name"]')  # 输入姓
    ck_time_zone_loc = (By.CSS_SELECTOR, 'input[placeholder="Please select time zone"')  # 选择时区
    st_time_zone_loc = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]')  # 选择时区
    ipt_imei_loc = (By.XPATH, '//*[@id="app"]/section/div[2]/div/form/div[6]/div/div/div[1]/input')  # 输入Imei号
    ipt_email_loc = (By.CSS_SELECTOR, 'input[placeholder="Enter email address"]')  # 输入邮箱
    ck_send_email_loc = (By.XPATH, '//*[@id="app"]/section/div[2]/div/form/div[7]/div[2]/button')  # 发送邮箱验证码
    ipt_email_code_loc = (By.CSS_SELECTOR, 'input[placeholder="Please enter Email verification code"]')  # 输入验证码
    ipt_payment_pwd_loc = (By.CSS_SELECTOR, 'input[placeholder="Please set up payment password"]')  # 输入支付密码
    ipt_confirm_payment_pwd_loc = (By.CSS_SELECTOR, 'input[placeholder="Please confirm the payment password"]')  # 输入支付密码
    ck_register_loc = (By.XPATH, '//span[.="Register"]')   # 点击注册

    '''点击注册后跳转注册成功页面'''
    ck_agree_loc =(By.XPATH, '//*[@id="app"]/section/section/div/div/div[3]/span/button[2]')
    txt_regist_suecces_msg =(By.XPATH, '//*[@id="app"]/section/div[2]/div/h2/i')
    txt_brand_number_msg =(By.XPATH, '//*[@id="pane-phone"]/div/form/div[1]/div/div/div[1]/input')  # 输入品牌号
    ipt_Return_login_loc =(By.XPATH, '//*[@id="app"]/section/div[2]/div/button')

    # 操作层
    def click_registration(self):
        """登陆界面点击注册"""
        self.driver.find_element(*self.ck_free_registration_loc).click()

    def select_business_category(self):
        """选择经营类型"""
        self.driver.find_element(*self.ck_business_loc).click()
        sleep(1)
        business_xpath = (By.XPATH, '//li[contains(., "Government")]')  # 定位经营类型
        self.driver.find_element(*business_xpath).click()

    def set_brand_name(self, value):
        """输入品牌名称"""
        self.driver.find_element(*self.ipt_brand_name_loc).send_keys(value)
        sleep(1)

    def setect_nation(self, nation, phone):
        """选择国家、输入手机号码、验证码"""
        self.driver.find_element(*self.ck_nation_loc).click()
        # nation_xpath = (By.XPATH, f'//span[contains(., "{nation}")]')  # 定位国家
        nation_xpath = (By.XPATH, f'//span[starts-with(., "{nation}")]')  # 定位国家
        self.driver.find_element(*nation_xpath).click()
        sleep(1)
        self.driver.find_element(*self.ipt_phone_number_loc).send_keys(phone)
        sleep(1)
        self.driver.find_element(*self.ck_sendsms_loc).click()
        sleep(3)
        self.driver.find_element(*self.ipt_sms_code_loc).send_keys('2222')

    def input_login_password(self, pwd, name, surname):
        """输入登录密码、姓、名"""
        self.driver.find_element(*self.ipt_pwd_loc).send_keys(pwd)
        self.driver.find_element(*self.ipt_confirm_pwd_loc).send_keys(pwd)
        self.driver.find_element(*self.ipt_name_loc).send_keys(name)
        self.driver.find_element(*self.ipt_surname_loc).send_keys(surname)

    def select_time_zone(self):
        """选择时区"""
        self.driver.find_element(*self.ck_time_zone_loc).click()
        sleep(2)
        # self.driver.find_element(*self.st_time_zone_loc).click()
        time_zone_xpath = (By.XPATH, '//li[contains(., "(GMT+08:00) China Standard Time - Shanghai")]')  # 定位时区
        self.driver.find_element(*time_zone_xpath).click()

    def input_imei(self, value):
        """输入imei"""
        self.driver.find_element(*self.ipt_imei_loc).send_keys(value)

    def input_email_address(self, value,):
        """输入邮箱"""
        self.driver.find_element(*self.ipt_email_loc).send_keys(value)
        sleep(1)
        """输入验证码"""
        self.driver.find_element(*self.ck_send_email_loc).click()
        sleep(3)
        self.driver.find_element(*self.ipt_email_code_loc).send_keys('2222')

    def input_payment_password(self, value):
        """输入支付密码"""
        self.driver.find_element(*self.ipt_payment_pwd_loc).send_keys(value)
        self.driver.find_element(*self.ipt_confirm_payment_pwd_loc).send_keys(value)

    def click_regisetr_laction(self):
        """点击同意注册"""
        self.driver.find_element(*self.ck_register_loc).click()
        sleep(2)
        self.driver.find_element(*self.ck_agree_loc).click()
        '''点击注册后跳转注册成功页面'''
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(self.txt_regist_suecces_msg, u"Registration success"))
        r = self.driver.find_element(*self.txt_regist_suecces_msg).text
        print(self.driver.find_element(*self.txt_brand_number_msg).text)  # 输入品牌号
        return r

    def click_return_login(self):
        """点击返回登陆按钮"""
        self.driver.find_element(*self.ipt_Return_login_loc).click()

if __name__ == '__main__':

    a = RegisterPage()
    a.open_url()
    a.click_registration()
    # a.select_business_category()
    # a.set_brand_name('测试')
    # a.input_login_password('Xgq111111','Xgq111111')
    # a.select_time_zone()
    # a.input_imei('351563020326924')
    # a.input_email_address(u'Toni@wokoworks.com')  # 输入邮箱，输入邮箱验证码
    a.input_payment_password(111111)  # 输入支付密码，输入确认支付密码
    a.setect_nation('Venezuela',4121999999)
    sleep(6)
    a.click_regisetr_laction()
    a.click_return_login()
