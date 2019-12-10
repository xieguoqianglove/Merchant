# coding:utf-8
import os
import logging
import time
import pymysql
import configparser

cur_path = os.path.dirname(os.path.realpath(__file__))  # 当前文件路径

# -------------------------------------------------------------------------------
# 函数/类/过程名称：Getdata
# 函数/类/过程目的：读取测试数据
# -------------------------------------------------------------------------------
def Getdata(title, subtitle):

    config = configparser.ConfigParser()  # 创建管理对象
    filename = os.path.join(cur_path, "test_data.ini")  # 测试数据文件

    config.read(filename)  # 读取数据文件
    if title not in config.sections():
        print('测试数据文件test_data.ini异常')
    elif subtitle not in config.options(title):
        print('%s配置项目下不存在%s元素，请检查配置文件test_data.ini' % (title, subtitle))
    else:
        setting = config.get(title, subtitle)
        return setting

# -------------------------------------------------------------------------------
# 函数/类/过程名称：InsertLog
# 函数/类/过程目的：写日志
# -------------------------------------------------------------------------------

log_path = os.path.join(os.path.dirname(cur_path), 'log')  # log_path是存放日志的路径
if not os.path.exists(log_path):  # 如果不存在这个log文件夹，就自动创建一个
    os.mkdir(log_path)

def InsertLog(name='root'):

    # 日志输出格式
    setmatter = '%(asctime)s => %(filename)s:%(funcName)s - %(levelname)s - %(message)s'
    datematter = '%Y-%m-%d %H:%M:%S'
    # 文件的命名
    logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d_%H'))
    # 创建logger日志器，如果name为空则返回root
    logger = logging.getLogger(name)
    # 设置日志等级：debug->info->warning->error
    logger.setLevel(logging.DEBUG)

    # 判断logger.handlers列表为空则添加，否则直接使用原handler处理器写日志
    if not logger.handlers:
        # 创建一个FileHandler，用于写到本地
        fh = logging.FileHandler(logname, encoding='utf-8')  # 若已有日志，则追加写入
        # 创建一个StreamHandler,用于输出到控制台
        ch = logging.StreamHandler()  # 将日志发送到Steam

        # 设置handlers处理器的日志输出格式
        formatter = logging.Formatter(fmt=setmatter, datefmt=datematter)
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 为logger日志器添加上创建好的处理器handlers
        logger.addHandler(fh)
        logger.addHandler(ch)

    # 这两行代码是为了避免日志输出重复问题
    #     logger.removeHandler(fh)
    #     logger.removeHandler(ch)
    return logger

# -------------------------------------------------------------------------------
# 函数/类/过程名称：ReadMobileMySQLData
# 函数/类/过程目的：获取手机号码的验证码
# -------------------------------------------------------------------------------
host = Getdata('Database_configuration','db_host')
portt = (Getdata('Database_configuration','db_port'))
user = Getdata('Database_configuration','db_user')
password = Getdata('Database_configuration','db_password')
db = Getdata('Database_configuration','db_table')

def ReadMobileMySQLData(sql):
    try:
        conn = pymysql.connect(host=host, port=portt,
                               user=user, password=password,
                               db=db,
                               charset='utf8',  # 对数据进行编码
                               cursorclass=pymysql.cursors.DictCursor  # 以字典形式展示数据库返回结果
                                 )
        curs = conn.cursor()  # 获取操作游标
        curs.execute(sql)     # 执行sql语句
        r = curs.fetchone()  # 获取返回所有的数据中的第一条
        # r = curs.fetchall()
        curs.close()
        conn.close()
        return r['code']
    except BaseException as msg:
        log = InsertLog()
        log.error(msg)

# -------------------------------------------------------------------------------
# 函数/类/过程名称：ReadEmailMySQLData
# 函数/类/过程目的：获取邮箱的验证码
# -------------------------------------------------------------------------------
def ReadEmailMySQLData(sql):
    try:
        conn = pymysql.connect(host=host, port=portt,
                               user=user, password=password,
                               db=db,
                               charset='utf8',  # 对数据进行编码
                               cursorclass=pymysql.cursors.DictCursor  # 以字典形式展示数据库返回结果
                               )
        curs = conn.cursor()  # 获取操作游标
        curs.execute(sql)     # 执行sql语句
        r = curs.fetchone()  # 获取返回所有的数据中的第一条
        # r = curs.fetchall()
        curs.close()
        conn.close()
        return r['code']
    except BaseException as msg:
        log = InsertLog()
        log.error(msg)

#-------------------------------------------------------------------------------
# 函数/类/过程名称：Screenshot
# 函数/类/过程目的：异常截图
#-------------------------------------------------------------------------------
def Screenshot(driver,picname):

    casepath = os.path.join(os.path.dirname(cur_path), './Img')  # casepath是存放截图的路径
    if not os.path.exists(casepath):  # 判断路径是否存在，如果不存在，创建文件夹
        os.mkdir(casepath)
    img_path = casepath + picname + '.png'
    driver.get_screenshot_as_file(img_path)

if __name__ == '__main__':
    print(cur_path)