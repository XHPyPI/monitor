# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-11-12 15:39:44
@UpdateDate: 2019-11-12 17:43:08
@Description: 性能监控使用
'''

from .monitor import start_monitor, end_monitor


def TestProfile():
    iCnt = 0
    for x in range(10000):
        iCnt += x
    print(iCnt)


if __name__ == "__main__":
    start_monitor("test-dir", "test-filename", ("time",))
    TestProfile()
    end_monitor()
