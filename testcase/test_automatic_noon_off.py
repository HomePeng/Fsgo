# -*- coding: utf-8 -*-

import sys, os
import pytest, time

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import *
from module.FSHome import FsHome
from tools.loggers import JFMlogging

logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@pytest.mark.run(order=1)
# 指定login先执行
class TestLogin:

    @pytest.mark.P0
    def test_init(self, scope="function"):
        logger.info("初始化进入考勤页面")
        self.home = FsHome(self.driver)
        self.home.appli()
        self.home.attendance()
        # self.home.CheckIn() 点击签到


