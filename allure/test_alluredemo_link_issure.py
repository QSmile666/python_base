# !/usr/bin/env python
# _*_ coding:utf-8 _*_

import allure

@allure.link("http://www.baidu.com", name="链接")
def test_with_link():
    print("这是一条加了链接的测试")
    pass

TEST_CASE_LINK = ""
@allure.testcase(TEST_CASE_LINK, '登录用例')
def test_with_testcase():
    print("这是一条测试用例的链接，链接到测试用例里面")
    pass
# --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
@allure.issue('140','这是一个issue')
def test_with_link():
    print("这是一条加了链接的测试")
    pass