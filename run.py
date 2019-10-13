# -*- coding: utf-8 -*-

import pytest, os, subprocess
import time
import datetime
from tools.loggers import JFMlogging

logger = JFMlogging().getloger()


def init_env():
    cmd = "python -m uiautomator2 clear-cache"
    subprocess.call(cmd, shell=True)
    cmd = "python -m uiautomator2 init"
    subprocess.call(cmd, shell=True)
    logger.info("初始化运行环境!")


def init_report():
    cmd = "allure generate --clean c -o reports"
    subprocess.call(cmd, shell=True)
    project_path = os.path.abspath(os.path.dirname(__file__))
    report_path = project_path + "/reports/" + "index.html"
    logger.info("报告地址:{}".format(report_path))


# init_env()
# pytest.main(["-s","testcase","--alluredir=data"])
# init_report()
if __name__ == '__main__':
    # 判断时间是否在时间范围内

    week = datetime.datetime.now().weekday()
    list = [0, 1, 2, 3, 4, 6]

    if week in list:
        if time.strftime("%H:%M") > '08:40' and time.strftime("%H:%M") < '22:45':
            pytest.main(["-s", "testcase"])
        elif time.strftime("%H:%M") > '12:02' and time.strftime("%H:%M") < '12:12':
            pass
        elif time.strftime("%H:%M") > '12:30' and time.strftime("%H:%M") < '12:40':
            pass
        elif time.strftime("%H:%M") > '18:17' and time.strftime("%H:%M") < '18:27':
            pass

