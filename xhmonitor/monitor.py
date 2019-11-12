# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-11-12 15:39:44
@UpdateDate: 2019-11-12 17:41:15
@Description: 性能监控
'''


import cProfile
import os
import pstats
import time

from pyprof2calltree import convert, visualize


__all__ = ["start_monitor", "end_monitor"]


class Monitor:

    _instance = None
    _profile = None

    __slots__ = ("dirs", "filename", "orderNames")

    def init(self):
        self.dirs = "Cache"
        self.filename = "%04d-%02d-%02d_%02d-%02d-%02d" % (time.localtime()[:6])
        self.orderNames = ("cumulative", "time")

    @staticmethod
    def instance():
        if not Monitor._instance:
            Monitor._instance = Monitor()
        return Monitor._instance

    def set_info(self, dirs: str="", filename: str="", orderNames: tuple=None):
        if dirs:
            self.dirs = dirs
        if filename:
            self.filename = filename
        if orderNames:
            self.orderNames = orderNames

    def start_monitor(self):
        if Monitor._profile:
            return
        self.init()
        Monitor._profile = cProfile.Profile()
        Monitor._profile.enable()

    def end_monitor(self):
        if not Monitor._profile:
            return
        Monitor._profile.disable()
        if not os.path.isdir(self.dirs):
            os.mkdir(self.dirs)

        txtpath = os.path.join(self.dirs, self.filename + ".txt")
        with open(txtpath, "wt") as f:
            st = pstats.Stats(Monitor._profile, stream=f)
            st.strip_dirs().sort_stats(*self.orderNames).print_stats()

        viewpath = os.path.join(self.dirs, self.filename + ".view")
        stats = Monitor._profile.getstats()
        visualize(stats)
        convert(stats, viewpath)

        Monitor._profile = None


def start_monitor(dirs: str="", filename: str="", orderNames: tuple=None):
    """开始性能监控
    Keyword Arguments:
        dirs {str} -- [保存的文件夹路径] (default: {"Cache"})
        filename {str} -- [保存的文件名不含后缀] (default: {"%Y-%m-%d %H:%M:%S"})
        orderNames {tuple} -- [stats排序] (default: {("cumulative", "time")})
    """
    Monitor.instance().start_monitor()
    Monitor.instance().set_info(dirs, filename, orderNames)


def end_monitor():
    Monitor.instance().end_monitor()
