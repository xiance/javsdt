# -*- coding:utf-8 -*-
from os import sep, makedirs, rename, symlink
import os
from os.path import exists
from shutil import copyfile

from javsdt.Functions.Record import record_video_old, record_fail


# 功能：2归类影片，只针对视频文件和字幕文件，无视它们当前所在文件夹
# 参数：设置settings，归类的目标目录路径root_classify，归类标准组合公式list_classify_basis，命名信息dict_data，处理的影片jav，已失败次数num_fail
# 返回：处理的影片jav（所在文件夹路径改变）、已失败次数num_fail
# 辅助：os.exists, os.rename, os.makedirs，
def classify_link_files(jav, num_fail, settings, dict_data, list_classify_basis, root_classify, list_name_video,
                        str_cd):
    # 如果需要归类，且不是针对文件夹来归类
    if settings.bool_classify and not settings.bool_classify_folder:
        # 移动的目标文件夹路径
        root_dest = root_classify + sep
        for j in list_classify_basis:
            # 针对演员不明的情况做特殊处理
            if '演员' in j and '演员' in dict_data[j]:
                continue
            else:
                root_dest += dict_data[j].rstrip()  # 【临时变量】归类的目标文件夹路径    C:\Users\JuneRain\Desktop\测试文件夹\葵司\
        # 演员名字以"_"分隔，可能出现连续两个无效演员名字的情况，需要将多余的"_"进行删除
        root_dest = str.replace(root_dest, '__', '_')
        # 如果以 '/' 结尾，则删除
        if root_dest.endswith(sep):
            root_dest = root_dest[0:-1]
        # 还不存在该文件夹，新建
        if not exists(root_dest):
            makedirs(root_dest)

        # 影片重命名的处理
        name_without_ext = ''
        for j in list_name_video:
            # 针对演员不明的情况做特殊处理
            if '演员' in j and '演员' in dict_data[j]:
                continue
            else:
                name_without_ext += dict_data[j]
        name_without_ext = str.replace(name_without_ext, '__', '_')
        name_without_ext += str_cd
        dict_data['视频'] = name_without_ext  # 【更新】 dict_data['视频']

        path_new = root_dest + sep + name_without_ext + jav.type  # 【临时变量】新的影片路径
        # 目标文件夹没有相同的影片，防止用户已经有一个“avop-127.mp4”，现在又来一个
        if not exists(path_new):
            rename(jav.path, path_new)
            symlink(jav.path, relpath(jav.root, path_new))
            print('    >归类视频文件完成')
            # 移动字幕
            if jav.subtitle:
                path_subtitle_new = root_dest + sep + name_without_ext + jav.subtitle_type  # 【临时变量】新的字幕路径
                if jav.path_subtitle != path_subtitle_new:
                    if not exists(path_subtitle_new):
                        copyfile(jav.path_subtitle, path_subtitle_new)
                    jav.subtitle = name_without_ext + jav.subtitle_type
                    # 不再更新 jav.path_subtitle，下面不会再操作 字幕文件
                    print('    >归类字幕文件完成')
            jav.root = root_dest  # 【更新】jav.root
        else:
            num_fail += 1
            record_fail('    >第' + str(num_fail) + '个失败！归类失败，重复的影片，归类的目标文件夹已经存在相同的影片：' + path_new + '\n')
            raise FileExistsError  # 【终止对该jav的整理】
    return jav, num_fail


def all_equal(elements):
    first_element = elements[0]
    for other_element in elements[1:]:
        if other_element != first_element: return False
    return True


def common_prefix(*sequences):
    if not sequences: return [], []
    common = []
    for elements in zip(*sequences):
        if not all_equal(elements): break
        common.append(elements[0])
    return common, [sequence[len(common):] for sequence in sequences]


def relpath(p1, p2, sep=os.path.sep, pardir=os.path.pardir):
    common, (u1, u2) = common_prefix(p1.split(sep), p2.split(sep))
    if not common:
        return p2
    return sep.join([pardir] * len(u1) + u2)
