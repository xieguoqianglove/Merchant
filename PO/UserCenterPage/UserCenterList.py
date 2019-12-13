from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PO.Page import Page
from PO.BasePage import Base
from time import sleep

class UserCenterList(Page, Base):
    """个人中心: 修改支付密码、登录密码、用户信息、退出"""

    # 对象层
    ck_usercenter_loc =(By.CSS_SELECTOR, 'i.el-icon-caret-bottom')  # 点击弹出用户中心
    # ck_user_info_loc = (By.XPATH, '//li[.="User information"]')   # 点击用户信息
    ck_user_info_loc = (By.XPATH, '//*[@id="app"]/section/div[1]/div/div[2]/div[1]/ul/li/div[2]/ul/li[1]')   # 点击用户信息
    txt_barnd_number_msg = (By.XPATH, '//*[@id="app"]/section/div[3]/div/div[2]/ul[2]/li[1]/div[1]')   # 获取品牌编号文本
    close_userinfo_Loc = (By.XPATH, '//*[@id="app"]/section/div[3]/div/div[1]/button')   # 关闭用户信息页面

    ck_loginpwd_loc = (By.XPATH, '//li[.="Modify login password"]')  # 修改登录密码
    ck_paypwd_loc = (By.XPATH, '//li[.="Modify Payment password"]')  # 修改支付密码
    ipt_old_pwd_loc = (By.XPATH, '//*[@class="changePassword"]/form/div[1]/div/div/div[1]/input')  # 输入旧密码
    ipt_new_pwd_loc = (By.XPATH, '//*[@class="changePassword"]/form/div[2]/div/div/div[1]/input')  # 输入新密码
    ipt_confirm_pwd_loc = (By.XPATH, '//*[@class="changePassword"]/form/div[3]/div/div/div[1]/input')  # 确认新密码
    ck_confirm_loc = (By.XPATH, '//span[.="Confirm"]')   # 点击确认
    txt_change_success_msg = (By.XPATH, '/html/body/div[3]/p')

    ck_sign_out_loc = (By.XPATH, '//li[.="Sign out"]')   # 点击退出登陆
    txt_PUNDIX_msg = (By.XPATH, '//*[@id="app"]/section/div[2]/div[1]/div[1]/p')  # 登录页面的 YOUR DIGITAL ASSETS PASS 文本

    # 操作层
    def click_user_information(self):
        """用户信息页面"""
        self.driver.find_element(*self.ck_user_info_loc).click()
        sleep(1)
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(self.txt_barnd_number_msg, 'Brand serial number:'))
        r = self.driver.find_element(*self.txt_barnd_number_msg).text
        self.driver.find_element(*self.close_userinfo_Loc).click()
        return r

    def click_exit_login(self):
        """退出登录"""
        self.driver.find_element(*self.ck_sign_out_loc).click()
        WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element(self.txt_PUNDIX_msg, u'YOUR DIGITAL ASSETS PASS'))
        return self.driver.find_element(*self.txt_PUNDIX_msg).text

    def click_login_password(self, text, text1):
        """修改登录密码"""
        self.driver.find_element(*self.ck_loginpwd_loc).click()
        sleep(1)
        self.driver.find_element(*self.ipt_old_pwd_loc).send_keys(text)
        self.driver.find_element(*self.ipt_new_pwd_loc).send_keys(text1)
        self.driver.find_element(*self.ipt_confirm_pwd_loc).send_keys(text1)
        self.driver.find_element(*self.ck_confirm_loc).click()
        if self.findElement('Please enter a new password (different from the old password) containing 8 characters, including one uppercase and one special character'):
            self.driver.refresh()
            return True

        # WebDriverWait(self.driver, 10).until(
        #     EC.text_to_be_present_in_element(self.txt_change_success_msg, u'Successfully modified')
        # return self.driver.find_element(*self.txt_change_success_msg).text

    def click_payment_password(self, text, text1):
        """修改支付密码"""
        self.driver.find_element(*self.ck_paypwd_loc).click()
        sleep(1)
        self.driver.find_element(*self.ipt_old_pwd_loc).send_keys(text)
        self.driver.find_element(*self.ipt_new_pwd_loc).send_keys(text1)
        self.driver.find_element(*self.ipt_confirm_pwd_loc).send_keys(text1)
        self.driver.find_element(*self.ck_confirm_loc).click()
        if self.findElement('Please enter a new password (6-digit) that is different from the old password'):
            self.driver.refresh()
            return True
        # else:
        #     WebDriverWait(self.driver, 10).until(
        #         EC.text_to_be_present_in_element(self.txt_change_success_msg, u'Successfully modified')
        #     return self.driver.find_element(*self.txt_change_success_msg).text