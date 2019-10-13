# -*- coding: utf-8 -*-
import sys, os

sys.path.append(os.getcwd())
import time
import subprocess
import uiautomator2  as ut2
from config import *
from tools.loggers import JFMlogging

logger = JFMlogging().getloger()


class Driver():

    def init_driver(self, device_name):
        '''
        初始化driver
        is_clear:清除数据
        :return:
        '''
        try:
            logger.info(device_name)
            d = ut2.connect(device_name)
            # 设置全局寻找元素超时时间
            d.wait_timeout = wait_timeout  # default 20.0
            # 设置点击元素延迟时间
            d.click_post_delay = click_post_delay
            logger.info("连接设备:{}".format(device_name))
            return d
        except Exception as e:
            logger.info("初始化driver异常!{}".format(e))
