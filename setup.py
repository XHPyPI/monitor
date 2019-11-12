# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-11-12 15:35:01
@UpdateDate: 2019-11-12 17:49:07
@Description: 发布包的配置
'''

import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setup(
    name='xhmonitor',
    version="0.0.2",
    author="lamborghini1993",
    author_email="1323242382@qq.com",
    description='a lib for Performance monitoring',
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://github.com/lamborghini1993/mypypi/tree/master/xhmonitor',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['pyprof2calltree'],
    python_requires='>=3.6',
)
