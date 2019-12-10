from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from PO.Page import Page
from PO.BasePage import Base

class LoginPage(Page,Base):

    # 对象层
    ck_phone_loc =(By.ID, "tab-phone")  # 手机登陆
    ipt_brand_loc = (By.XPATH, '//*[@id="pane-phone"]/div/form/div[1]/div/div/div[1]/input')  # 输入品牌号
    ck_nation_loc = (By.CSS_SELECTOR, 'input[placeholder="Country/Region"]')  # 点击选择国家
    ipt_phone_number_loc = (By.CSS_SELECTOR, 'input.el-input__inner:nth-child(2)')  # 输入手机号码
    ck_phone_send_loc = (By.XPATH, '//*[@id="pane-phone"]/div/form/div[3]/button')  # 发送验证码
    ipt_phone_code_loc = (By.XPATH, '//*[@id="pane-phone"]/div/form/div[3]/div/div/div/input')  # 输入验证码
    ipt_phone_pwd_loc = (By.XPATH, '//*[@id="pane-phone"]/div/form/div[4]/div/div/div/input')  # 输入登陆密码
    btn_phone_login_loc = (By.XPATH, '//*[@id="pane-phone"]/div/form/div[5]/div/div/button')  # 点击登陆

    # 邮箱登陆
    ck_email_loc = (By.ID, "tab-email")  # 邮箱登陆
    ipt_email_brand_loc = (By.XPATH, '//*[@id="pane-email"]/div/form/div[1]/div/div/div[1]/input')  # 输入品牌号
    ipt_email_loc = (By.XPATH, '//*[@id="pane-email"]/div/form/div[2]/div/div/div[1]/input')  # 输入邮箱
    ck_email_send_loc = (By.XPATH, '//*[@id="pane-email"]/div/form/div[3]/button')  # 发送验证码
    ipt_email_code_loc = (By.XPATH, '//*[@id="pane-email"]/div/form/div[3]/div/div/div/input')  # 输入验证码
    ipt_email_pwd_loc = (By.XPATH, '//*[@id="pane-email"]/div/form/div[4]/div/div/div/input')  # 输入登陆密码
    btn_email_login_loc = (By.XPATH, '//*[@id="pane-email"]/div/form/div[5]/div/div/button')  # 点击登陆

    get_login_success_msg = (By.XPATH, '//*[@id="app"]/section/div[1]/div/div[1]/div[2]/ul/li[1]')  # Home文本

    '''登录成功后进行中文英文切换'''
    ipt_English_loc = (By.CSS_SELECTOR, '.lang-but')
    ipt_zhongwen_loc = (By.XPATH, '//*[@id="app"]/section/div[1]/div/div[2]/div[3]/ul/li/div[2]/ul/li[1]')
    ipt_Home_loc = (By.XPATH, '//*[@id="app"]/section/div[1]/div/div[1]/div[2]/ul/li[1]')

    # 登录页面切换成中文版本
    ipt_English1_loc = (By.XPATH, '/html/body/div/section/div[1]/div/div[2]/div/ul/li/div[1]/button')
    ipt_zhongwen1_loc = (By.XPATH, '/html/body/div/section/div[1]/div/div[2]/div/ul/li/div[2]/ul/li[1]')


    def setect_nation(self, nation, phone):
        """选择国家"""
        self.driver.find_element(*self.ck_nation_loc).click()
        nation_xpath = (By.XPATH, f'//li[contains(., "{nation}")]')  # 定位国家
        self.driver.find_element(*nation_xpath).click()
        sleep(1)
        self.driver.find_element(*self.ipt_phone_number_loc).send_keys(phone)
        sleep(1)

    def phone_login(self, brand, nation, phone, pwd):
        """手机登陆流程"""
        self.driver.find_element(*self.ipt_brand_loc).send_keys(brand)
        self.setect_nation(nation, phone)
        self.driver.find_element(*self.ck_phone_send_loc).click()
        sleep(3)
        self.driver.find_element(*self.ipt_phone_code_loc).send_keys('2222')
        self.driver.find_element(*self.ipt_phone_pwd_loc).send_keys(pwd)
        self.driver.find_element(*self.btn_phone_login_loc).click()

    def email_login(self, brand, email, pwd):
        """邮箱登陆流程"""
        self.driver.find_element(*self.ck_email_loc).click()
        self.driver.find_element(*self.ipt_email_brand_loc).send_keys(brand)
        self.driver.find_element(*self.ipt_email_loc).send_keys(email)
        self.driver.find_element(*self.ck_email_send_loc).click()
        sleep(3)
        self.driver.find_element(*self.ipt_email_code_loc).send_keys('2222')
        self.driver.find_element(*self.ipt_email_pwd_loc).send_keys(pwd)
        self.driver.find_element(*self.btn_email_login_loc).click()

    # 操作层
    def click_English1_swith(self):
        sleep(1)
        self.driver.find_element(*self.ipt_English1_loc).click()
        sleep(3)
        a = self.driver.find_element(*self.ipt_zhongwen1_loc)
        action_a = ActionChains(self.driver)
        action_a.move_to_element(a).click().perform()

    def login_success_msg(self):
        """登陆成功页面包含Home文本"""
        r = self.driver.find_element(*self.get_login_success_msg).text
        return r

if __name__ == '__main__':

    obj = LoginPage()
    obj.open_url()
    obj.setect_nation('Venezuela',4121999999)
    sleep(5)