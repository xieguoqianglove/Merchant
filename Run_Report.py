import os,time
import unittest
from BeautifulReport import BeautifulReport

# 获取测试用例文件夹路径
curpath = os.path.dirname(os.path.realpath(__file__))

class RunReport:
    """
    输出报告
    """

    def __init__(self):
        # 测试用例位置
        self.case_path = os.path.join(curpath, "Scripts")
        print(f'执行的测试用例路径为：{self.case_path}')

    def add_cases(self):
        """
        批量添加测试用例
        :return:
        """

        discover = unittest.defaultTestLoader.discover(self.case_path, pattern="*_tc.py",
                                                       top_level_dir=None)
        return discover

    def run_cases_by_beautiful_report(self, cases):
        """
        借用BeautifulReport模版输出测试用例报告
        :param cases:测试用例集
        :return:
        """
        day = time.strftime('%Y-%m-%d')
        result = BeautifulReport(cases)
        result.report(filename='%s_report.html' % day,
                      description='自动化测试报告',
                      log_path='Reports')


if __name__ == "__main__":
    # 用例集合
    re = RunReport()
    cases = re.add_cases()
    re.run_cases_by_beautiful_report(cases)
