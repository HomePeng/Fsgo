# -*- coding: utf-8 -*-
import uiautomator2 as u2


def init_driver(IP, debug=False):
    d = u2.connect(IP)
    print(d.info)
    d.debug = debug
    return d
