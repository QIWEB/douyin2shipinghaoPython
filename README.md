# douyin2shipinghaoPython
自动爬取抖音个人账户全部视频，自动去水印下载，自动保存封面，全自动登录微信短视频，发布短视频， 短视频运营神器
#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
by qiweb
技术微信：qiweb3
关注，收藏 一下
视频号：老王de日常
视频号ID:sphMlB0G4vnMbrU

公众号：QIWEB精品共享科技
bilibili 我的站功能演示 最靓的噢
自动爬取抖音个人账户全部视频，自动去水印下载，自动保存封面，全自动登录微信短视频，发布短视频， 短视频运营神器
https://www.bilibili.com/video/BV1D34y1h7M5?spm_id_from=333.999.0.0
2022年5月11日22:04:46
功能：
1、自动爬取一个抖音用户的全部短视频 保存
2、自动发布 微信短视频 支持续传
'''

from selenium import webdriver
import pathlib
import hashlib
import requests # 数据请求模块 第三方模块 pip install requests
import re # 正则表达式模块 内置模块
import time # 时间模块
from selenium import webdriver # selenium
