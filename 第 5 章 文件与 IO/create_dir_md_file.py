#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 用来创建对应文件夹 及 readme.md
"""
import os

__author__ = '__L1n__w@tch'


def get_all_dir_name():
    result_dir = list()
    with open("readme.md", "rt") as f:
        for each_line in f:
            if each_line.startswith("*"):
                dir_name = each_line.lstrip("* ").rstrip()
                result_dir.append(dir_name)
    return result_dir


def run():
    # 读取同目录下的 readme.md, 获取所有文件夹名称
    dirs = get_all_dir_name()

    # 遍历所有文件夹, 判断文件夹是否存在, 如果不存在则创建文件夹, 存在则判断 md 文件是否存在, 不存在则创建
    for each_dir in dirs:
        if os.path.exists(each_dir) and os.path.exists("{}/readme.md".format(each_dir)):
            continue
        else:
            os.makedirs(each_dir, exist_ok=False)
            with open("{}/readme.md".format(each_dir), "xt") as f:
                f.write("### {}".format(each_dir))


if __name__ == "__main__":
    run()
    print("[*] 创建完毕")
