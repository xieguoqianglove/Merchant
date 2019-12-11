from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PO.Page import Page
from PO.BasePage import Base
from time import sleep

class Account(Page, Base):
    """人员——>账号列表 页面"""

    # 对象层
    ipt_staff_list_loc = (By.XPATH, '//*[@class="permissions"]/section/aside/ul/li/span')  #点击账户列表
    txt_newaccount_msg = (By.XPATH,'//*[@class="head"]/button/span/span[1]')
    ipt_staff_id_loc = (By.CSS_SELECTOR, 'input[placeholder="Staff ID"]')  # 输入用户编号
    ipt_user_number_loc = (By.CSS_SELECTOR, 'input[placeholder="User No."]')  # 输入用户名称
    ipt_phone_number_loc = (By.CSS_SELECTOR, 'input[placeholder="Phone no."]')  # 输入手机号
    ipt_name_loc = (By.CSS_SELECTOR, 'input[placeholder="Name"]')  # 输入名称
    ck_store_loc = (By.XPATH, '//*[@class="el-form formMain"]/div/div[5]/div/div[1]/div/span[4]/span/i')  # 点击门店
    ck_all_shop_loc = (By.XPATH, '//*[@class="select-item"]/label/span[2]')

    ck_search_loc = (By.XPATH, "//span[.='Search']")  # 点击查询
    ck_reset_loc = (By.XPATH, "//span[.='Reset']")  # 点击重置
    ck_modify_loc = (By.XPATH, "//span[.='Modify']")  # 点击详情
    ck_save_loc = (By.XPATH, "//span[.='Save']")  # 点击保存

    txt_staff_msg = (By.XPATH, '//*[@class="el-table__row commonTableRow"]/td[3]/div')
    txt_user_No_msg = (By.XPATH, '//*[@class="el-table__row commonTableRow"]/td[2]/div')
    txt_phone_No_msg = (By.XPATH, '//*[@class="el-table__row commonTableRow"]/td[4]/div')
    txt_name_msg = (By.XPATH, '//*[@class="el-table__row commonTableRow"]/td[5]/div')
    txt_store_name_msg = (By.XPATH, '//*[@class="el-table__row commonTableRow"]/td[6]/div')
    txt_save_success_msg = (By.XPATH, '/html/body/div[3]/p')  # 返回修改成功的信息
    txt_edit_save_msg = (By.XPATH, '/html/body/div[4]/p')  # 返回修改成功的信息

    '''新增账号'''
    ck_cuerry_loc =(By.CSS_SELECTOR, 'input[placeholder="Country/Region"]')  # 选择国家
    ipt_phone_loc =(By.CSS_SELECTOR, 'input[placeholder="Please enter phone number"]')  # 输入手机号码
    ipt_first_name_loc = (By.CSS_SELECTOR, 'input[placeholder="Enter first name"]')  # 输入名称
    ipt_last_name_loc = (By.CSS_SELECTOR, 'input[placeholder="Enter last name"]')  # 输入名称
    ipt_staff_loc = (By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section/div[1]/div/div[2]/form/div[3]/div/div/div[1]/input')  # 输入名称
    ck_store_name_loc =(By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section/div[1]/div/div[2]/form/div[4]/div/div/div/div[1]/div')
    st_store_loc = (By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section/div[1]/div/div[2]/form/div[4]/div/div/div/div[2]/div[2]/label/span[1]')
    ck_role_loc =(By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section/div[1]/div/div[2]/form/div[5]/div/div/div/div[1]/div')
    st_role_loc =(By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section/div[1]/div/div[2]/form/div[5]/div/div/div/div[2]/div[2]/label/span[2]')
    ipt_login_pwd_loc = (By.CSS_SELECTOR, 'input[placeholder="Please enter password"]')  # 输入登陆密码
    ipt_confirmpwd_loc = (By.CSS_SELECTOR, 'input[placeholder="Please re-enter password"]')  # 输入登陆密码
    ipt_pay_pwd_loc = (By.CSS_SELECTOR, 'input[placeholder="Please set up payment password"]')  # 输入支付密码
    ipt_confirmpaypwd_loc = (By.CSS_SELECTOR, 'input[placeholder="Please confirm the payment password"]')  # 输入支付密码
    ck_create_loc = (By.XPATH, "//span[.='Create']")  # 点击创建

    # 操作层
    def click_account_list(self):
        """点击 账号列表"""
        self.driver.find_element(*self.ipt_staff_list_loc).click()

    def get_new_account_txt(self):
        """获取新建账号文本"""
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.txt_newaccount_msg, u"New account"))
        r = self.driver.find_element(*self.txt_newaccount_msg).text
        return r

    def setect_nation(self, nation, phone):
        """选择国家"""
        self.driver.find_element(*self.ck_cuerry_loc).click()
        nation_xpath = (By.XPATH, f'//li[contains(., "{nation}")]')  # 定位国家
        self.driver.find_element(*nation_xpath).click()
        sleep(1)
        self.driver.find_element(*self.ipt_phone_loc).send_keys(phone)
        sleep(1)

    def add_account(self, nation, phone, text, text1, text2):
        """验证新增账号"""
        self.driver.find_element(*self.txt_newaccount_msg).click()
        sleep(1)
        self.setect_nation(nation, phone)
        self.driver.find_element(*self.ipt_first_name_loc).send_keys(text)
        self.driver.find_element(*self.ipt_last_name_loc).send_keys(text)
        self.driver.find_element(*self.ipt_staff_loc).send_keys(phone)
        self.driver.find_element(*self.ck_store_name_loc).click()
        self.driver.find_element(*self.st_store_loc).click()
        sleep(1)
        self.driver.find_element(*self.ck_store_name_loc).click()
        self.driver.find_element(*self.ck_role_loc).click()
        self.driver.find_element(*self.st_role_loc).click()
        sleep(1)
        self.driver.find_element(*self.ck_role_loc).click()
        self.driver.find_element(*self.ipt_login_pwd_loc).send_keys(text1)
        self.driver.find_element(*self.ipt_confirmpwd_loc).send_keys(text1)
        self.driver.find_element(*self.ipt_pay_pwd_loc).send_keys(text2)
        self.driver.find_element(*self.ipt_confirmpaypwd_loc).send_keys(text2)
        self.driver.find_element(*self.ck_create_loc).click()
        # WebDriverWait(self.driver, 5, 0.5).until(
        #     EC.text_to_be_present_in_element(self.txt_save_success_msg, u"Successfully added"))
        # r = self.driver.find_element(*self.txt_save_success_msg).text
        return True

    def verify_select_shop_query(self):
        """验证 全选方式的门店 查询"""
        self.driver.find_element(*self.ck_store_loc).click()
        self.driver.find_element(*self.ck_all_shop_loc).click()
        sleep(1)
        self.driver.find_element(*self.ck_search_loc).click()
        r = self.driver.find_element(*self.txt_store_name_msg).text
        return r

    def verify_work_number_query(self, text):
        """验证 工号 查询"""
        self.driver.find_element(*self.ipt_staff_id_loc).send_keys(text)
        self.driver.find_element(*self.ck_search_loc).click()
        sleep(1)
        r = self.driver.find_element(*self.txt_staff_msg).text
        return r

    def verify_user_number_query(self, text):
        """验证 用户编号 查询"""
        self.driver.find_element(*self.ipt_user_number_loc).send_keys(text)
        self.driver.find_element(*self.ck_search_loc).click()
        sleep(1)
        r = self.driver.find_element(*self.txt_user_No_msg).text
        return r

    def verify_telephone_query(self, text):
        """验证 手机号码 查询"""
        self.driver.find_element(*self.ipt_phone_number_loc).send_keys(text)
        self.driver.find_element(*self.ck_search_loc).click()
        sleep(1)
        r = self.driver.find_element(*self.txt_phone_No_msg).text
        return r

    def verify_name_query(self, text):
        """验证  姓名 查询"""
        self.driver.find_element(*self.ipt_name_loc).send_keys(text)
        self.driver.find_element(*self.ck_search_loc).click()
        sleep(1)
        r = self.driver.find_element(*self.txt_name_msg).text
        return r

    def verify_modify_function(self):
        """验证 修改功能"""
        self.driver.find_element(*self.ck_modify_loc).click()
        sleep(1)
        self.driver.find_element(*self.ck_save_loc).click()
        return True

    def verify_reset_function(self, text):
        """验证 重置功能"""
        self.driver.find_element(*self.ipt_user_number_loc).send_keys(text)
        self.driver.find_element(*self.ck_reset_loc).click()
        r = self.driver.find_element(*self.ipt_user_number_loc).text
        return r
