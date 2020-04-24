# !/usr/bin/env python
# _*_ coding:utf-8 _*_

import allure
import pytest

def test_attach_text():
    allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach("<body>这是一段html body块</body>", "html测试块", attachment_type=allure.attachment_type.HTML)

# 实践之后，图片展示不出来
def test_attach_photo():
    allure.attach.file("/Users/mac/PycharmProjects/python_base/allure/resource/容器云平台GYT-HD-1.6.24-20200422上线计划.png",name="这是一个图片", attachment_type=allure.attachment_type.PNG)