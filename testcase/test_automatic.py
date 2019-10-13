# -*- coding: utf-8 -*-

import sys, os
import pytest, time

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import *
from tools.loggers import JFMlogging

logger = JFMlogging().getloger()


@pytest.mark.usefixtures('driver_setup')
@pytest.mark.run(order=1)
# 指定login先执行
class TestLogin:

    @pytest.fixture()
    def init(self, scope="function"):
        pass


    @pytest.mark.P0
    def test_login(self, init):
        init.login()
