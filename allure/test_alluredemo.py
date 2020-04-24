# !/usr/bin/env python
# _*_ coding:utf-8 _*_

import pytest

def test_success():
    # this test success
    assert True

def test_failure():
    # this test failure
    assert False

def test_skip():
    # this test is skipped
    pytest.skip("for a reason!")

def test_broken():
    raise Exception("oops")




# class TestAllureDemo():
#     def setup(self):
#         pass
#
#     def teardown(self):
#         pass
#
#     def test_allureDemo(self):
#         pass

