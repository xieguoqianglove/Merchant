# -*- coding: utf-8 -*-
# @file: DigitalCurrencyRecordList.py
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from po.Page import Page

class DigitalCurrencyRecord(Page):
    '''报表--数字货币记录 页面'''

    # 对象层
    ipt_DigitalCurrencyRecordList_loc = (By.XPATH, '//*[@id="app"]/section/div[2]/div/div/section/section/aside/ul/li[3]')
    txt_Digital_record_msg_loc = (By.XPATH,'//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section[2]/main/div[1]/h2')
    ipt_start_day_loc = (By.CSS_SELECTOR,'input[placeholder="开始日期"]')
    ipt_end_day_loc = (By.CSS_SELECTOR,'input[placeholder="结束日期"]')
    txt_trading_time_msg = (By.XPATH,'//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section[2]/main/div[3]/div/div[3]/table/tbody/tr[1]/td[8]/div/span')
    ck_query_loc = (By.XPATH,'//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section[2]/main/form/div[1]/div[3]/div/div/div/button')
    ck_reset_loc = (By.XPATH,'//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section[2]/main/form/div[1]/div[4]/div/div/div/button')
    ck_shop_loc = (By.XPATH,'//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section[2]/main/form/div[1]/div[2]/div/div[1]/div')
    st_quanxuan_shop_loc = (By.XPATH,'//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section[2]/main/form/div[1]/div[2]/div/div[2]/div[2]/label/span[1]/span')
    ipt_ck_shop_loc = (By.XPATH,'//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section[2]/main/form/div[1]/div[2]/div/div[2]/div[2]/div/label[9]')
    txt_shop_msg = (By.XPATH,'//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section[2]/main/div[3]/div/div[3]/table/tbody/tr[1]/td[9]/div')
    ipt_shop_loc = (By.XPATH,'//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section[2]/main/form/div[1]/div[2]/div/div[2]/div[1]/div/input')
    ipt_trading_number_loc =(By.CSS_SELECTOR,'input[placeholder="交易流水号"]')
    txt_trading_number_msg =(By.XPATH,'//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section[2]/main/div[3]/div/div[3]/table/tbody/tr[1]/td[1]/div')
    ipt_order_number_loc =(By.CSS_SELECTOR,'input[placeholder="订单号"]')
    txt_order_number_msg =(By.XPATH,'//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section[2]/main/div[3]/div/div[3]/table/tbody/tr[1]/td[2]/div')
    ck_cashier_loc =(By.CSS_SELECTOR,'input[placeholder="收银员"]')
    ck_first_cashier_loc =(By.XPATH,'/html/body/div[2]/div[1]/div[1]/ul/li[1]')
    txt_cashier_msg =(By.XPATH,'//*[@id="app"]/section/div[2]/div/div/section/section/section/main/section/section[2]/main/div[3]/div/div[3]/table/tbody/tr[1]/td[7]/div')

    # 操作层
    def click_DigitalCurrencyRecordList(self):
        '''点击 现金记录 '''
        self.dv.find_element(*self.ipt_DigitalCurrencyRecordList_loc).click()

    def get_Digital_record_msg_txt(self):
        '''获取 数字货币记录 文本'''
        WebDriverWait(self.dv, 10, 0.5).until(
            EC.text_to_be_present_in_element(self.txt_Digital_record_msg_loc, u"数字货币记录"))
        r = self.dv.find_element(*self.txt_Digital_record_msg_loc).text
        return r

    def verify_input_shop_query(self,text):
        '''验证 输入方式的门店 查询  '''
        self.dv.find_element(*self.ck_shop_loc).click()
        self.dv.find_element(*self.ipt_shop_loc).send_keys(text)
        sleep(1)
        self.dv.find_element(*self.ipt_ck_shop_loc).click()
        self.dv.find_element(*self.ck_query_loc).click()
        WebDriverWait(self.dv, 5, 0.5).until(
            EC.text_to_be_present_in_element(self.txt_shop_msg, u'%s'%text))
        r = self.dv.find_element(*self.txt_shop_msg).text
        return r

    def verify_select_shop_query(self):
        '''验证 选择方式的门店 查询  '''
        self.dv.find_element(*self.ck_shop_loc).click()
        self.dv.find_element(*self.st_quanxuan_shop_loc).click()
        sleep(1)
        self.dv.find_element(*self.ck_query_loc).click()
        r = self.dv.find_element(*self.txt_shop_msg).text
        return r

    def verify_reset_function(self,text):
        '''验证 重置功能'''
        self.dv.find_element(*self.ipt_trading_number_loc).send_keys(text)
        self.dv.find_element(*self.ck_reset_loc).click()
        r = self.dv.find_element(*self.ipt_trading_number_loc).text
        return r

    def verify_day_query(self,text,text1):
        '''验证 日期查询'''
        self.dv.find_element(*self.ipt_start_day_loc).send_keys(text)
        self.dv.find_element(*self.ipt_end_day_loc).send_keys(text1)
        sleep(1)
        r = self.dv.find_element(*self.txt_trading_time_msg).text
        return r

    def verify_trading_number(self,text):
        '''验证 交易流水号 查询'''
        self.dv.find_element(*self.ipt_trading_number_loc).send_keys(text)
        self.dv.find_element(*self.ck_query_loc).click()
        sleep(1)
        r = self.dv.find_element(*self.txt_trading_number_msg).text
        return r

    def verify_order_number(self,text):
        '''验证 订单号 查询'''
        self.dv.find_element(*self.ipt_order_number_loc).send_keys(text)
        self.dv.find_element(*self.ck_query_loc).click()
        r = self.dv.find_element(*self.txt_order_number_msg).text
        return r

    def verify_cashier(self):
        '''验证 收银员 查询,默认选择第一个'''
        self.dv.find_element(*self.ck_cashier_loc).click()
        self.dv.find_element(*self.ck_first_cashier_loc).click()
        r = self.dv.find_element(*self.txt_cashier_msg).text
        return r

    def close_broser(self):
        self.dv.quit()