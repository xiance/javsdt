# -*- coding:utf-8 -*-
from os import sep, makedirs, rename, symlink
import os
from os.path import exists
from shutil import copyfile
from configparser import RawConfigParser

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
        new_folder = ''
        for j in list_classify_basis:
            # 针对演员不明的情况做特殊处理
            if '演员' in j and '演员' in dict_data[j]:
                continue
            else:
                new_folder += dict_data[j].rstrip()  # 【临时变量】归类的目标文件夹路径    C:\Users\JuneRain\Desktop\测试文件夹\葵司\
        # 演员名字以"_"分隔，可能出现连续两个无效演员名字的情况，需要将多余的"_"进行删除
        new_folder = str.replace(new_folder, '__', '_')
        # 如果以 '/' 结尾，则删除
        if new_folder.endswith(sep):
            new_folder = new_folder[0:-1]
        # 如果以 '_' 结尾，则删除
        if new_folder.endswith('_'):
            new_folder = new_folder[0:-1]

        root_dest += new_folder
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
            symlink(relpath(jav.root, path_new), jav.path)
            jav.name = name_without_ext + jav.type
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


# 功能：6为当前jav收集演员头像到“.actors”文件夹中
# 参数：演员们 list_actors，jav当前所处文件夹的路径root_now
# 返回：无
# 辅助：os.path.exists，os.makedirs, configparser.RawConfigParser, shutil.copyfile
def collect_sculpture_fix(list_actors, root_now):
    for each_actor in list_actors:
        path_exist_actor = '演员头像' + sep + each_actor[0] + sep + each_actor  # 事先准备好的演员头像路径
        if exists(path_exist_actor + '.jpg'):
            pic_type = '.jpg'
        elif exists(path_exist_actor + '.png'):
            pic_type = '.png'
        else:
            config_actor = RawConfigParser()
            config_actor.read('【缺失的演员头像统计For Kodi】.ini', encoding='utf-8-sig')
            try:
                if not config_actor.has_section('缺失的演员头像'):
                    config_actor.add_section('缺失的演员头像')
                if config_actor.has_option('缺失的演员头像', each_actor):
                    each_actor_times = config_actor.get('缺失的演员头像', each_actor)
                    config_actor.set("缺失的演员头像", each_actor, str(int(each_actor_times) + 1))
                else:
                    config_actor.set('缺失的演员头像', each_actor, '1')
            except:
                config_actor.set("缺失的演员头像", each_actor, '1')
            config_actor.write(open('【缺失的演员头像统计For Kodi】.ini', "w", encoding='utf-8-sig'))
            continue
        # 已经收录了这个演员头像
        root_dest_actor = root_now + sep + '.actors' + sep  # 头像的目标文件夹
        if not exists(root_dest_actor):
            makedirs(root_dest_actor)
        # 复制一份到“.actors”
        copyfile(path_exist_actor + pic_type, root_dest_actor + each_actor + pic_type)
        print('    >演员头像收集完成：', each_actor)


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
