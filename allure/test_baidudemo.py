# !/usr/bin/env python
# _*_ coding:utf-8 _*_

import allure
import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


@allure.testcase("http://www.baidu.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize("test_data1", ['allure', 'pytest', 'unittest'])
def test_steps_demo(test_data1):
    with allure.step("打开百度"):
        base_url = "http://www.baidu.com"
        driver = webdriver.Chrome()
        driver.get(base_url)
        driver.maximize_window()
        driver.implicitly_wait(3)

    with allure.step(f"输入搜索内容：{test_data1}"):
        # 找到搜索框，输入test_data1内容
        driver.find_element(By.ID, "kw").send_keys(test_data1)
        time.sleep(2)

    with allure.step("点击'百度一下'进行搜索"):
        # 找到"百度一下"按钮，点击搜索
        driver.find_element(By.ID, "su").click()
        time.sleep(2)

    with allure.step("保存截图"):
        # 保存截图
        pic_path = "./resultPic/b.png"
        driver.save_screenshot(pic_path)
        allure.attach.file(pic_path, attachment_type=allure.attachment_type.PNG)
        allure.attach("<head></head><body>首页</body>", "Attach with HTML type", allure.attachment_type.HTML)

    with allure.step("关闭浏览器"):
        driver.quit()
