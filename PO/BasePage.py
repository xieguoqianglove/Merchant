from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException
from libs.ShareModules import Getdata
import os,time
import random,string

class Base:
    """
    页面的公共元素操作
    """

    # -------------------------------元素的公共方法------------------------------- #
    def __init__(self, driver):
        self.driver = driver

    def findElement(self, el):
        """
        判断某元素是否存在
        :return:
        """

        source = self.driver.page_source  # 打印当前页面全部的元素
        if el in source:
            return True
        else:
            print('找不到该元素...')
            return False

    def get_size(self):
        """
        获取屏幕分辨率大小
        :return:
        """
        size = self.driver.get_window_size()
        print(size['width'], size['height'])
        return size['width'], size['height']

    def swipeUP(self, element):
        """
        滑动到顶部
        :return:
        """
        self.driver.find_element(*element).send_keys(Keys.UP)

    def swipeDown(self,element):
        """
        滑动到底部
        :return:
        """
        self.driver.find_element(*element).send_keys(Keys.DOWN)

    def wait_element(self,element):
        """
        等待元素出现，默认等待10秒，0.5毫秒扫描一次
        :param element: 元素(部分或者全部元素内容)
        :return:
        """
        get_error_msg = (By.CSS_SELECTOR, 'p.el-message__content')  # 提示语
        try:
            WebDriverWait(self.driver, 10, 0.5).until(
                EC.text_to_be_present_in_element(get_error_msg, element))
            return True
        except:
            return False

    def upload_img_path(picname):
        """
        上传文件的路径
        :return:
        """
        return os.path.abspath(os.path.dirname(os.getcwd())) + '/PO/AddCardPage/upload_img/' + '%s.png' % picname

    def save_img(self, picname):
        """
        截图并保存
        :param picname:文件名
        :使用例子：self.obj.save_img('003_password_error')
        """
        # path = os.path.abspath(os.path.dirname(os.getcwd())) + '/Img/'
        path = Getdata('pictures', 'path')
        if not os.path.exists(path):
            os.mkdir(path)
        self.driver.get_screenshot_as_file(path + picname + '.png')

    def is_toast_exist(self, text):
        """
        定位toast提示语
        :param text: 提示语内容（全部）
        :param timeout: 多少秒后超时，不再监控
        :param poll_frequency: 监控间隔
        :return:
        """
        try:
            toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)

            WebDriverWait(self.driver, 10, 0.2).until(
                EC.presence_of_element_located(toast_loc))
            return True
        except:
            return False

    def click_text(self, text):
        """
        特殊点击法，点击一些只有text标识的元素
        :param text: 元素名称
        :return:
        """

        try:
            # text_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
            text_loc = ("xpath", f'//*[text()="{text}"]')
            self.driver.find_element(*text_loc).click()
        except:
            raise AttributeError('不存在该元素...')


    def send_keys_text(self,el,text):
        """
        特殊点击法，点击一些只有text标识的元素
        :param el: 元素名称
        :text: 输入内容
        :return:
        """

        try:
            text_loc = ("xpath", ".//*[contains(@text,'%s')]" % el)
            self.driver.find_element(*text_loc).send_keys(text)
        except:
            raise AttributeError('不存在该元素...')

    def clear_and_sendkeys(self, sendtexts, *loc):
        """
        先清除当前文本框内的文字再输入新的文字
        :param sendtexts:要输入的新的文字
        :return:None
        """
        webelement = self.driver.find_element(*loc)
        webelement.clear()
        webelement.send_keys(sendtexts)


    def action_chains_send_keys(self,element,text):
        """
        方法使用介绍：ActionChains创建鼠标事件,move_to_element鼠标移动到某个元素,click单击鼠标左键,
        send_keys发送某个键到当前焦点的元素,perform执行鼠标事件
        :param element: 查找的元素
        :param text: 需要输入的信息
        :return:
        """
        a = self.driver.find_element(element)
        action_a = ActionChains(self.driver)
        action_a.move_to_element(a).click().send_keys(text).perform()


    # -------------------------------随机生成数据部分,用于注册------------------------------- #
    def create_mobile():
        """
        随机生成电话号码
        :return:
        """

        num = '0123456789'
        # code = ['+86137', '+86159', '+86188', '+86132']  # 中国
        code = ['4120', '4123', '4124']  # 委内瑞拉
        mobile = random.choice(code) + ''.join(random.choice(num) for i in range(6))  # 委内瑞拉
        return mobile

    def create_email():
        """
        随机生成邮箱地址
        :return:
        """

        num = '0123456789'
        server = '@qq.com', '@163.com'  # 邮箱域名
        email = ''.join(random.choice(num) for i in range(8)) + random.choice(server)
        return email

    def create_address(size=8, chars=string.digits + string.ascii_letters + string.digits):
        """
        随机生成字符串（字母+数字）
        :param size: 随机生产字符串的长度
        :param chars: 字符串范围（字母+数字)
        :return:
        """

        return ''.join(random.choice(chars) for _ in range(size))

    def create_string(size=8, chars=string.ascii_letters):
        """
        随机字符串
        :return:
        """

        return ''.join(random.choice(chars) for _ in range(size))


if __name__ == '__main__':

    print(Base.create_address(8))