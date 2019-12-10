from libs.ShareModules import Getdata
from selenium import webdriver

test_url = Getdata('Merchant_url', 'url')

# 配置浏览器类型，默认谷歌
bs = 'gc'
def create_browser_driver(b = bs):
    try:
        if b == 'gc':
            driver = webdriver.Chrome()
        elif b == 'ff':
            driver = webdriver.Firefox()
        elif b == 'ie':
            driver = webdriver.Ie()
        else:
            pass
        return driver
    except Exception:
        pass

class Page():
    def __init__(self, driver=''):

        b = driver
        if b == '':
            self.driver = create_browser_driver()
        else:
            self.driver = b
        # self.driver.maximize_window()
        self.driver.set_window_size(1600,1400)
        # print(self.driver.get_window_size())
        self.driver.implicitly_wait(5)  # 隐式等待

    def open_url(self, url=test_url):
        self.driver.get(url)

    def close_broser(self):
        self.driver.quit()
