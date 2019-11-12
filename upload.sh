#!/bin/bash
# @Author: lamborghini1993
# @Description: 一键打包pypi并上传

python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
