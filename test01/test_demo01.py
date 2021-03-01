# -*- coding:utf-8 -*-

import pytest


def test_py01():
    print("demo_test_py01方法执行...")


def test_py02():
    print("demo_test_py02方法执行...")


class TestDemo01:
    def test_01(self):
        print()
        print("demo_test01执行了")
        assert "hello" == "hello"

    def test_02(self):
        assert 100 == 100
        print("demo_test02执行了")

    def test_03(self):
        print("demo_test03执行了")
        # assert "hello" == "hello word"


if __name__ == '__main__':
    pytest.main(["-s", "test_demo01.py"])
