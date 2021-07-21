# -*- coding=utf-8 -*-
import time

import pytest

import allure


@allure.feature("获取 auto 接口")
class TestAuto1(object):
    def setup(self):
        print("setup......start")

    def setup_class(self):
        print("setup_class.....start")

    @allure.story("正常获取 auto1")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_001(self):
        time.sleep(5)
        a = 1
        assert a == 1

    def test_002(self):
        time.sleep(5)
        d = 5
        assert d == 5

    def test_003(self):
        time.sleep(5)
        e = 7
        assert e == 7

    def teardown(self):
        print("teardown.....end")

    def teardown_class(self):
        print("teardown_class.....end")


if __name__ == '__main__':
    pytest.main(["-s"])
