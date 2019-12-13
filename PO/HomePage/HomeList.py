from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PO.Page import Page
from PO.BasePage import Base

class Home(Page, Base):
    """首页--首页页面"""

    # 对象层
    ck_Home_loc = (By.XPATH, '//*[@id="app"]/section/div[1]/div/div[1]/div[2]/ul/li[1]')
    txt_Business_income_today_msg_loc = (By.XPATH, "//*[@id='app']/section/div[2]/div/div/section/div[1]/div[2]/div[1]/div")

    # 操作层
    def click_HomePage(self):
        """点击首页"""
        self.driver.find_element(*self.ck_Home_loc).click()

    def get_Business_income_today_msg(self):
        """获取页面上今日营业收入文本"""
        WebDriverWait(self.driver, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.txt_Business_income_today_msg_loc, u"Today's income"))
        return self.driver.find_element(*self.txt_Business_income_today_msg_loc).text

    # 业务层
    def HomePageBusiness(self):
        self.click_HomePage()
        self.get_Business_income_today_msg()

