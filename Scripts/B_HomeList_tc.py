
from time import sleep
import unittest
from libs.ShareBusiness import login_B
from libs.ShareModules import InsertLog
from PO.Pagetitle import PageTitle
from PO.HomePage.HomeList import Home
from BeautifulReport import BeautifulReport

class HomeListTest(unittest.TestCase):
    """测试 首页 页面"""

    def setUp(self):
        self.a = login_B()
        self.b = PageTitle(self.a)
        self.c = Home(self.a)

    def tearDown(self):
        # sleep(40)  # 防止提示验证码发送过快
        self.c.close_broser()

    @BeautifulReport.add_img('HomeListTest_001_Home_fail')
    def test_001_Check_page(self):
        """
        用例一 ：检查页面是否正常
        """
        try:
            self.b.switch_to_HomePage()
            sleep(1)
            self.c.click_HomePage()
            self.assertTrue(self.c.get_Business_income_today_msg())
        except (BaseException, AssertionError) as msg:  # BaseException所有异常的基类,AssertionError断言语句失败
            self.c.save_img('HomeListTest_001_Home_fail')
            InsertLog().debug(msg)
            raise BaseException

if __name__ == '__main__':
    unittest.main(verbosity=2)