from selenium.webdriver.common.by import By
from PO.Page import Page
from libs.ShareBusiness import login_B
from time import sleep

class PageTitle(Page):
    """切换商户后台的主菜单"""

    # 对象层
    ipt_HomePage_loc = (By.XPATH, '//*[@id="app"]/section/div[1]/div/div[1]/div[2]/ul/li[1]')
    ipt_ShopPage_loc = (By.XPATH, '//*[@id="app"]/section/div[1]/div/div[1]/div[2]/ul/li[2]')
    ipt_PersonnelPage_loc = (By.XPATH, '//*[@id="app"]/section/div[1]/div/div[1]/div[2]/ul/li[3]')
    ipt_DevicePage_loc = (By.XPATH, '//*[@id="app"]/section/div[1]/div/div[1]/div[2]/ul/li[4]')
    ipt_OrderPage_loc = (By.XPATH, '//*[@id="app"]/section/div[1]/div/div[1]/div[2]/ul/li[5]')
    ipt_ReportFormPage_loc = (By.XPATH, '//*[@id="app"]/section/div[1]/div/div[1]/div[2]/ul/li[6]')
    ipt_AssetsPage_loc = (By.XPATH, '//*[@id="app"]/section/div[1]/div/div[1]/div[2]/ul/li[7]/span')
    ipt_User_CenterPage_loc = (By.XPATH, '//*[@id="app"]/section/div[1]/div/div[2]/div[1]/ul')

    # 操作层
    def switch_to_HomePage(self):
        """切换到首页页面"""
        self.driver.find_element(*self.ipt_HomePage_loc).click()

    def switch_to_ShopPage(self):
        """切换到门店页面"""
        self.driver.find_element(*self.ipt_ShopPage_loc).click()

    def switch_to_PersonnelPage(self):
        """切换到人员页面"""
        self.driver.find_element(*self.ipt_PersonnelPage_loc).click()

    def switch_to_DevicePage(self):
        """切换到设备页面"""
        self.driver.find_element(*self.ipt_DevicePage_loc).click()

    def switch_to_OrderPage(self):
        """切换到订单页面"""
        self.driver.find_element(*self.ipt_OrderPage_loc).click()

    def switch_to_ReportFormPage(self):
        """切换到报表页面"""
        self.driver.find_element(*self.ipt_ReportFormPage_loc).click()

    def switch_to_AssetsPage(self):
        """切换到资产界面"""
        self.driver.find_element(*self.ipt_AssetsPage_loc).click()

    def switch_to_Personal_CenterPage(self):
        """切换到个人中心"""
        sleep(1)
        self.driver.find_element(*self.ipt_User_CenterPage_loc).click()
        sleep(1)

    def close_broser(self):
        self.driver.quit()

if __name__ == '__main__':
    c = login_B()
    a = PageTitle(c)
    a.open_url()
    a.switch_to_HomePage()
    a.switch_to_OrderPage()
    a.switch_to_PersonnelPage()
    a.close_broser()