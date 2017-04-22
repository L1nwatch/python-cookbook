#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" 用来创建对应文件夹 及 readme.md
"""
import os
from itertools import dropwhile

__author__ = '__L1n__w@tch'


def update_summary_md_file(dirs):
    # 获取当前是第几章
    current_dir = os.path.dirname(__file__)
    current_dir_name = os.path.basename(current_dir)

    # 获取根目录路径
    root_dir = os.path.dirname(os.path.dirname(__file__))

    # 创建要更新的内容
    update_content = list()
    update_content.append("* [{current_dir}]({current_dir}/readme.md)\n".format(current_dir=current_dir_name))
    for each_dir in dirs:
        update_content.append("{sep}* [{each_dir}]({current_dir}/{each_dir}/readme.md)\n".format(
            sep=" " * 4, each_dir=each_dir, current_dir=current_dir_name))

    # 开始修改 summary.md
    with open("{}/SUMMARY.md".format(root_dir), "rt+") as f:
        # 跳过非本章内容, 或者直到文件结尾
        for line in dropwhile(lambda each_line: current_dir_name not in each_line, f):
            # 开始更新
            # 依次判断要更新的内容是否已经存在, 存在则离开队列
            if line == update_content[0]:
                update_content.pop(0)
        for each_content in update_content:
            f.write(each_content)


def get_all_dir_name():
    result_dir = list()
    with open("readme.md", "rt") as f:
        for each_line in f:
            if each_line.startswith("*"):
                dir_name = each_line.lstrip("* ").rstrip()
                result_dir.append(dir_name)
    return result_dir


def run():
    print("[*] 开始创建文件夹及对应的 md 文件")
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

    print("[*] 开始更新根目录下的 SUMMARY.md 文件")
    update_summary_md_file(dirs)


if __name__ == "__main__":
    run()
    print("[*] 脚本执行完毕")
