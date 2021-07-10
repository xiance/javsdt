# -*- coding:utf-8 -*-
from os import system
from configparser import RawConfigParser
from traceback import format_exc

try:
    print('>>正在重写ini文件...')
    config_settings = RawConfigParser()
    config_settings.add_section("收集nfo")
    config_settings.set("收集nfo", "是否跳过已存在nfo的文件夹？", "否")
    config_settings.set("收集nfo", "是否收集nfo？", "是")
    config_settings.set("收集nfo", "nfo中title的格式", "车牌+空格+标题")
    config_settings.set("收集nfo", "是否去除标题末尾的演员姓名？", "否")
    config_settings.set("收集nfo", "额外将以下元素添加到特征中", "系列、片商")
    config_settings.set("收集nfo", "是否将特征保存到genre？", "是")
    config_settings.set("收集nfo", "是否将特征保存到tag？", "是")
    config_settings.add_section("重命名影片")
    config_settings.set("重命名影片", "是否重命名影片？", "是")
    config_settings.set("重命名影片", "重命名影片的格式", "车牌+空格+标题")
    config_settings.add_section("修改文件夹")
    config_settings.set("修改文件夹", "是否重命名或创建独立文件夹？", "是")
    config_settings.set("修改文件夹", "新文件夹的格式", "【+全部演员+】+车牌")
    config_settings.add_section("归类影片")
    config_settings.set("归类影片", "是否归类影片？", "否")
    config_settings.set("归类影片", "针对文件还是文件夹？", "文件夹")
    config_settings.set("归类影片", "归类的根目录", "所选文件夹")
    config_settings.set("归类影片", "归类的标准", "影片类型\全部演员")
    config_settings.add_section("下载封面")
    config_settings.set("下载封面", "是否下载封面海报？", "是")
    config_settings.set("下载封面", "DVD封面的格式", "视频+-fanart.jpg")
    config_settings.set("下载封面", "海报的格式", "视频+-poster.jpg")
    config_settings.set("下载封面", "是否为海报加上中文字幕条幅？", "否")
    config_settings.set("下载封面", "是否为海报加上无码流出条幅？", "否")
    config_settings.add_section("字幕文件")
    config_settings.set("字幕文件", "是否重命名已有的字幕文件？", "是")
    config_settings.set("字幕文件", "是否跳过已有字幕的影片？", "是")
    config_settings.add_section("kodi专用")
    config_settings.set("kodi专用", "是否收集演员头像？", "否")
    config_settings.set("kodi专用", "是否对多cd只收集一份图片和nfo？", "否")
    config_settings.add_section("emby/jellyfin")
    config_settings.set("emby/jellyfin", "网址", "http://localhost:8096/")
    config_settings.set("emby/jellyfin", "API ID", "b55d950becc74bbebbf4698d995db826")
    config_settings.set("emby/jellyfin", "是否覆盖以前上传的头像？", "否")
    config_settings.add_section("局部代理")
    config_settings.set("局部代理", "是否使用局部代理？", "否")
    config_settings.set("局部代理", "http还是socks5？", "http")
    config_settings.set("局部代理", "代理端口", "127.0.0.1:10809")
    config_settings.set("局部代理", "是否代理javlibrary（有问题）？", "否")
    config_settings.set("局部代理", "是否代理javbus？", "否")
    config_settings.set("局部代理", "是否代理jav321？", "否")
    config_settings.set("局部代理", "是否代理javdb？", "否")
    config_settings.set("局部代理", "是否代理arzon？", "否")
    config_settings.set("局部代理", "是否代理dmm图片？", "否")
    # config_settings.set("其他设置", "是否将全部演员（多个）表现为“n人共演？", "否")
    config_settings.add_section("原影片文件的性质")
    config_settings.set("原影片文件的性质", "有码素人无视多余的字母数字", "xhd1080、mm616、fhd-1080")
    config_settings.set("原影片文件的性质", "无码无视多余的字母数字", "1080p、caribbean、carib、1pondo、1pon、fhd、all、tokyo-hot、tokyohot、3xplanet、full")
    config_settings.set("原影片文件的性质", "是否中字即文件名包含", "-C、_C、中字、中文字幕、字幕")
    config_settings.set("原影片文件的性质", "是否中字的表现形式", "㊥")
    config_settings.set("原影片文件的性质", "是否流出即文件名包含", "流出")
    config_settings.set("原影片文件的性质", "是否流出的表现形式", "无码流出")
    config_settings.set("原影片文件的性质", "有码", "有码")
    config_settings.set("原影片文件的性质", "无码", "无码")
    config_settings.set("原影片文件的性质", "素人", "素人")
    config_settings.set("原影片文件的性质", "FC2", "FC2")
    config_settings.add_section("信息来源")
    config_settings.set("信息来源", "是否用javlibrary整理影片时收集网友的热评？", "是")
    config_settings.add_section("其他设置")
    config_settings.set("其他设置", "简繁中文？", "简")
    config_settings.set("其他设置", "javlibrary网址", "https://www.b47w.com/")
    config_settings.set("其他设置", "javbus网址", "https://www.buscdn.me")
    config_settings.set("其他设置", "javdb网址", "https://javdb9.com/")
    config_settings.set("其他设置", "扫描文件类型", "mp4、mkv、avi、wmv、iso、rmvb、flv、ts")
    config_settings.set("其他设置", "重命名中的标题长度（50~150）", "50")
    config_settings.add_section("百度翻译API")
    config_settings.set("百度翻译API", "是否将翻译简介为中文？", "否")
    config_settings.set("百度翻译API", "app id", "")
    config_settings.set("百度翻译API", "密钥", "")
    config_settings.add_section("百度人体分析")
    config_settings.set("百度人体分析", "是否需要准确定位人脸的poster？", "否")
    config_settings.set("百度人体分析", "appid", "")
    config_settings.set("百度人体分析", "api key", "")
    config_settings.set("百度人体分析", "secret key", "")
    config_settings.write(open('【点我设置整理规则】.ini', "w", encoding='utf-8-sig'))
    print('    >“【点我设置整理规则】.ini”重写成功！')
    ####################################################################################################################
    config_actor = RawConfigParser()
    config_actor.add_section("缺失的演员头像")
    config_actor.set("缺失的演员头像", "演员姓名", "N(次数)")
    config_actor.add_section("说明")
    config_actor.set("说明", "上面的“演员姓名 = N(次数)”的表达式", "后面的N数字表示你有N部(次)影片都在找她的头像，可惜找不到")
    config_actor.set("说明", "你可以去保存一下她的头像jpg到“演员头像”文件夹", "以后就能保存她的头像到影片的文件夹了")
    config_actor.write(open('actors_for_kodi.ini', "w", encoding='utf-8-sig'))
    print('    >“actors_for_kodi.ini”重写成功！')
    system('pause')
except:
    print(format_exc())
    print('\n创建ini失败，解决上述问题后，重新打开exe创建ini！')
    system('pause')
