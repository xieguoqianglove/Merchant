import zmail
from Run_Report import RunReport
import os,time
from libs.ShareModules import Getdata

dd = time.strftime('%Y-%m-%d', time.localtime(time.time()))

# 获取报告文件夹路径
curpath = os.path.dirname(os.path.realpath(__file__))

def get_file():
    """
    获取报告文件绝对地址
    若不存在则产生测试报告
    """

    filepath = os.path.join(curpath, 'Reports/')  # 获取报告文件夹路径
    print(f'输出的测试报告路径为：{filepath}')
    f = os.listdir(filepath)  # 列出该文件夹的所有文件
    dex = dd + '_report.html'

    if dex in f:
        file = filepath + dd + '_report.html'
    else:
        print('还未存在当前日期的测试报告')
        print('开始产生测试报告...')
        report = RunReport()
        cases = report.add_cases()
        report.run_cases_by_beautiful_report(cases)  # 运行cases产生报告
        file = filepath + dd + '_report.html'
    return file

# 邮件内容
mail_content = {'subject': '%s 自动化测试报告' % dd, 'headers': 'Dear',
                'attachments': get_file()}

"""读取测试数据"""
sender = Getdata('EmailSetting', 'sender')   # 邮箱地址
password = Getdata('EmailSetting', 'psw')    # 客户端授权密码
server = zmail.server(sender, password)      # 使用账号和密码登陆邮箱

# 发送邮件
receivers = Getdata('EmailSetting', 'receiveuser')  # 获取接收邮件人
server.send_mail(receivers.split(','), mail_content)
print('%s 发送邮件成功' % dd)