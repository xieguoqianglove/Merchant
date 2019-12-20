from time import sleep
import unittest
from libs.ShareBusiness import login_C
from libs.ShareModules import InsertLog
from PO.Pagetitle import PageTitle
from PO.DevicePage.DeviceList import Device
from libs.ShareModules import Getdata
from BeautifulReport import BeautifulReport
'''读取测试数据'''
device_imei = Getdata('DeviceList_tc', 'device_imei')
shop_name = Getdata('ShopList_tc', 'shop_name')

class DeviceListTest(unittest.TestCase):
    """测试设备列表 页面"""

    @classmethod
    def setUpClass(self):
        self.a = login_C()
        self.b = PageTitle(self.a)
        self.c = Device(self.a)

    @classmethod
    def tearDownClass(self):
        self.c.close_broser()

    def DeviceBusiness(self):
        self.b.switch_to_ReportFormPage()
        sleep(1)
        self.b.switch_to_DevicePage()
        sleep(1)
        self.c.click_DeviceList()

    @BeautifulReport.add_img('DeviceListTest_001_check_page_fail')
    def test_001_Check_page(self):
        """
        用例一 ：检查页面是否正常
        """
        try:
            self.b.switch_to_DevicePage()
            sleep(1)
            self.c.click_DeviceList()
            self.assertTrue(self.c.get_DeviceId_msg_txt())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('DeviceListTest_001_check_page_fail')
            InsertLog().error(msg)
            raise BaseException

    @BeautifulReport.add_img('DeviceListTest_002_store_search_fail')
    def test_002_Verify_input_shop_query(self):
        """
        用例二 ：验证门店查询
        """
        try:  # 传参 需要查询的门店名称
            self.DeviceBusiness()
            self.assertTrue(self.c.input_shop_query(shop_name))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('DeviceListTest_002_store_search_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('DeviceListTest_003_device_Imei_fail')
    def test_003_Verify_DeviceIMEI(self):
        """
        用例三 ：验证设备IMEI查询
        """
        try:  # 传参 需要查询的设备IMEI
            self.DeviceBusiness()
            self.assertTrue(self.c.verify_device_imei_query(device_imei))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('DeviceListTest_003_device_Imei_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('DeviceListTest_004_device_status_fail')
    def test_004_Verify_Device_LockState(self):
        """
        用例四 ：验证设备锁定状态查询
        """
        try:
            self.DeviceBusiness()
            self.assertTrue(self.c.verify_device_lock_status_query())
        except (BaseException, AssertionError) as msg:
            self.c.save_img('DeviceListTest_004_device_status_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('DeviceListTest_005_reset_fail')
    def test_005_Verify_Reset(self):
        """
        用例五 ：验证重置功能
        """
        try:  # 传参任意,先输入设备imei、点击重置
            self.DeviceBusiness()
            self.assertIn('', self.c.verify_reset_function(device_imei))  # 重置成功则返回空字符串
        except (BaseException, AssertionError) as msg:
            self.c.save_img('DeviceListTest_005_reset_fail')
            InsertLog().debug(msg)
            raise BaseException

    @BeautifulReport.add_img('DeviceListTest_006_edit_fail')
    def test_006_Verify_Edit_Success(self):
        """
        用例六 ：验证编辑成功后返回信息
        '"""
        try:
            self.DeviceBusiness()
            self.assertTrue(self.c.verify_edit_success(shop_name))
        except (BaseException, AssertionError) as msg:
            self.c.save_img('DeviceListTest_006_edit_fail')
            InsertLog().debug(msg)
            raise BaseException


if __name__ == '__main__':
    unittest.main(verbosity=2)