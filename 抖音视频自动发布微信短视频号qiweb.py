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

后续会继续加入 抖音去水印 自动发布抖音和其他平台的自动化，自动筛选视频功能  技术交流微信908701702
'''

from selenium import webdriver
import pathlib
import hashlib
import requests # 数据请求模块 第三方模块 pip install requests
import re # 正则表达式模块 内置模块
import time # 时间模块
from selenium import webdriver # selenium

#浏览器对象
driver = webdriver.Firefox()

# 基本信息
# 视频存放路径
catalog_mp4 = r"e:\Desktop\视频发布"
# 视频描述
describe = "裸眼3D看蜘蛛侠 #搞笑 #电影 #视觉震撼"

path_mp4=None

#已经下载的记录
is_down_listfile="is_down_list.txt"
#已经发布
is_push_file='is_push_list.txt'
#公众号urls
urls=["https://mp.weixin.qq.com/s/GgvO3CHMdu0abnj3p-7qGQ"]

#md5记录重复
def get_md5_value(src):
    myMd5 = hashlib.md5()
    myMd5.update(src)
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest

# 写文件保存记录
def saveFile(file_name, info):
    with open(file_name, 'a', encoding="utf-8") as f:
        f.write(str(info) + "\n")
        print('保存成功：', info)

#获取单个抖音视频并下载
def getDuyin(urlX,titlex,img):
    url = 'https://www.douyin.com/video/6881953434883329293'
    if urlX:
        url=urlX

    f=open(is_down_listfile,'r',encoding='utf-8')
    if get_md5_value(titlex.encode("utf-8")) in f.read():
        print("此视频已经下载过，不重复下载:"+titlex)
        return

    headers = {
        'Cookie':'douyin.com; ttwid=1%7CALm1AdkJN9MoABG4paN9gNOO5rPA_uQtSG43d114Qs8%7C1650973544%7C8dc4627c11931d6daf2178fa4328885f138a98daa2ab8e35eda4d336e3bfb005; passport_csrf_token=b3f072d4690b8e26850d3914bf30286f; passport_csrf_token_default=b3f072d4690b8e26850d3914bf30286f; MONITOR_WEB_ID=3bf2a2a1-3626-48ca-a5ec-670f846ad249; d_ticket=87f851ade84dfd0677a64da7261eb3dd73e8c; n_mh=8nysT__BxDL_VpPZTRMYKZZSN1pywPhZ9o63MSmzGLg; passport_auth_status=3404239d038c0c981d830cf094a68336%2C; passport_auth_status_ss=3404239d038c0c981d830cf094a68336%2C; sso_auth_status=2b0d47f05bc4234d095437a53050cdae; sso_auth_status_ss=2b0d47f05bc4234d095437a53050cdae; _tea_utm_cache_1300=undefined; _tea_utm_cache_2285=undefined; _tea_utm_cache_6383=undefined; IS_HIDE_THEME_CHANGE=1; THEME_STAY_TIME=299673; FOLLOW_LIVE_POINT_INFO=MS4wLjABAAAAhC8cCbfe9dAycEtiZ3LCVbG3FPrW46adgY7vpr0-IaPimcumki2DCxWKk7ecW3Pq%2F1651680000000%2F0%2F1651664308051%2F0; s_v_web_id=verify_l2riae9g_8vIkEycb_a1NH_4xHU_BzAM_JGHtnOqQJd4b; odin_tt=bb9335f88e211a3208b75df4d54f518ff77e64098a26469b47cd5fd2dbb0644a2e067b193cb14d0259f6ec13d7ca763789f24ddd3d7341e985779e4f8ca9c10a; pwa_guide_count=3; __ac_nonce=0627afc1400fb00dfaa27; __ac_signature=_02B4Z6wo00f01qyDPHgAAIDBHHLQsoQfod6sozjAAMlmPE0RCx2EbHvVDq800veI78cW1SyycLzZ32s9-mTWK4ALtVehfUCvpV6MneDdPpRd-SseI-umrTJl-0lKsgBPl39WoGeHFVsM26Dwc5; strategyABtestKey=1652227106.086; home_can_add_dy_2_desktop=1; tt_scid=fvd-z6NRLJVuASD7Dwk497Z0RfYd9O.Js2PfnVfwTn-oHDi6o314LOi6KWgX28eqac9c; msToken=5MRxMyIgDZG0lqVe4mYCZYzocc7cTgOec8ffsdVJYW1jCfTAm9A3Z30EX49Mh3Nm4A_KN3vvqganOSPR2ss3bA_6GtUIAWR9dedSscCpT7tiPWlrrzfKH9N4YR1ptFpn; msToken=PxZpZX0EQtNYvcH4MiOL_thcWfTAhe5ZxFBbiMqL31B-g4ntaTpfqncg7MwvsYJ8TN3R-DMsoVk9bTtCDl28HTFYRjmccmCVncapw0CxHdrfoXRBzsE7lrAx30MyLau8',
        'Referer':'https: // www.douyin.com /',
        'User-Agent':'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.125 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    #print(response.text) 调试用
    html_data = re.findall('src(.*?)%3Fa%3D', response.text)
    print(html_data)
    html_data=html_data[1]
    video_url = requests.utils.unquote(html_data).replace('":"', 'https:')
    print(video_url)
    title=None
    if titlex:
        title=titlex
    else:
        title = re.findall('<title data-react-helmet="true">(.*?)</title>', response.text)[0]
    #下载视频
    video_content = requests.get(url=video_url).content
    new_title = re.sub(r'[\/:*?"<>|]', '', title).replace('dou',"").replace('抖音','')
    with open(catalog_mp4+'\\'+new_title  + '.mp4', mode='wb') as f:
        f.write(video_content)

    #下载封面
    imgx = requests.get(url=img).content
    with open(catalog_mp4+'\\'+new_title  + '.jpg', mode='wb') as f:
        f.write(imgx)

    # 保存记录
    saveFile(is_down_listfile, get_md5_value(title.encode("utf-8")) + "|")
    print(title,'下载完成')

#自动下拉加载网页
def drop_down():
    #执行页面滚动的操作""” # javascript
    for x in range(1, 30, 4):#1 3 5 79 在你不断的下拉过程中，页面高度也会变的
        time.sleep(1)
        j =x / 9 #1/9 3/9 5/9 9/9
        # document.documentElement.scrollTop 指定滚动条的位置
        # document.documentElement.scrollHeight获取浏览器页面的最大高度
        js ='document.documentElement.scrollTop = document.documentElement.scrollHeight * %f'% j
        driver.execute_script(js)

#批量下载抖音号主页视频
def batch_download_v(is_drop_down,user_url='https://www.douyin.com/user/MS4wLjABAAAABc_SL7XZf0M3S08RjjtuTY0Rl8o5T-C7pmq0QLK7j9mgpeaXblBlKpdnsObViLJJ'):
    driver.get(user_url)
    time.sleep(5)
    #是否滑动 获取当前用户全部
    if is_drop_down:
        drop_down()
    lis = driver.find_elements_by_css_selector('#root > div > div.T_foQflM > div > div > div.ckqOrial > div.mwbaK9mv > div:nth-child(2) > ul > li')
    print(lis)
    for li in lis:
        href = li.find_element_by_css_selector('a').get_attribute('href')
        img=li.find_element_by_css_selector('img')
        imgsrc=img.get_attribute("src")
        title=img.get_attribute('alt')
        print(href,title,imgsrc)
        #单个视频采集
        getDuyin(href,title,imgsrc)


#获取当前日期
def get_now_time():
    """
    获取当前日期时间
    :return:当前日期时间
    """
    now =  time.localtime()
    now_time = time.strftime("%Y-%m-%d %H:%M:%S", now)
    return now_time

#开始根据视频地址上传
def publish_shipinhao(path_mp4):
    '''
     作用：发布微信视频号
    '''
    #文件名
    mp4_file_name = path_mp4.split("\\")[-1]

    # 封面地址获取
    img_src=mp4_file_name.replace('.mp4','.jpg')

    #视频描述
    describe=mp4_file_name.replace(".mp4",'@老王De日常').replace("DOU","").replace("抖音","")

    f=open(is_push_file,'r',encoding='utf-8')
    if get_md5_value(describe.encode("utf-8")) in f.read():
        print("此视频已经发表过，不重复发布")
        return

    #打开也没后点发布视频
    while True:
        time.sleep(3)
        try:
            # # 点击发布
            driver.find_element_by_xpath('//*[text()="发表动态"]').click()
            break;
        except Exception as e:
            #print(e)
            print("视频打开发表页面·")


    print("start input")
    driver.find_element_by_xpath('//input[@type="file"]').send_keys(path_mp4)


    #出现删除说明上传成功
    while True:
        time.sleep(1)
        try:
            # # 点击发布
            driver.find_element_by_xpath('//*[text()="删除"]')
            break;
        except Exception as e:
            #print(e)
            print("视频打开发表页面·")

    # 等待视频上传完成

    time.sleep(3)
    print("视频已上传完成！")


    # 描述
    element = driver.find_element_by_xpath('//*[@data-placeholder="添加描述"]')
    element.click()  # 模拟鼠标点击
    # sleep(2)
    driver.implicitly_wait(5)
    # sleep(1)
    driver.switch_to.active_element.send_keys(describe[::-1])


    # 添加位置
    driver.find_element_by_xpath('//*[@class="position-display-wrap"]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[text()="不显示位置"]').click()

    element = driver.find_element_by_xpath('//*[@placeholder = "将公众号文章链接或红包封面链接粘贴在此处"]')
    element.click()  # 模拟鼠标点击
    # sleep(2)
    driver.implicitly_wait(5)
    driver.switch_to.active_element.send_keys(urls[0])

    # 人工进行检查并发布
    time.sleep(2)
    # # 点击发布
    driver.find_element_by_xpath('//*[text()="发表"]').click()
    #保存已经发布记录
    saveFile(is_push_file,get_md5_value(describe.encode("utf-8")) )
    file_handle = open('push_log.txt', mode ='a+',encoding="utf-8").write(str(get_now_time()+" 成功上传 "+mp4_file_name+"\n"))

#单元测试
#saveFile(is_down_listfile,"百坭老黄：这算不算损友😂？@抖音小助手 #我太难了😂 #搞笑 #幽默搞笑 #农村搞笑段子 #意不意外 #搞笑视频"+"|")
#src = '百坭老黄：这算不算损友😂？@抖音小助手 #我太难了😂 #搞笑 #幽默搞笑 #农村搞笑段子 #意不意外 #搞笑视频'
#result_md5_value = get_md5_value(src.encode("utf-8"))
#result_sha1_value = get_sha1_value(src.encode("utf-8"))
#print(result_md5_value)
#print(result_sha1_value)

#x='e:\Desktop\视频发布\M灵梦🍋：#不眨眼vlog #美女 #cosplay #二次元 .mp4'
#print(x.split("\\")[-1])
print(get_now_time())
#open('push_log.txt', mode ='a+',encoding="utf-8").write(str(get_now_time()+" 成功上传 "+"我爱你.mp4\n"))
#file_handle = open('push_log.txt', mode ='a+',encoding="utf-8").write(str(get_now_time()+" 成功上传 "+"我爱你.mp4"))
#time.sleep(222)

#batch_download_v(False,'https://www.douyin.com/user/MS4wLjABAAAAMnZvXiKmE5rQD5X0YRfxnKbxEFpTw-IxsR137FxBqKYNjR2m39OTCXlichfyL2nA')
#batch_download_v(True,'https://www.douyin.com/user/MS4wLjABAAAAOb1v4Y9IgeRdrVAlDgBSsLtCsuZX36gstiXststnLqo')
# 开始执行视频发布
path = pathlib.Path(catalog_mp4)
print(1)
# 视频地址获取
path_mp4 = ""


# 进入微信视频号创作者页面，并上传视频
driver.get("https://channels.weixin.qq.com/platform/post/create")  # https://channels.weixin.qq.com/platform/post/create
time.sleep(23)
import random
for i in path.iterdir():
    if (".mp4" in str(i)):
        path_mp4 = str(i)
        #break 发不完一个稍微停几秒别太快被系统检测到了
        time.sleep(random.randint(1,3))
        if (path_mp4 != ""):
            print("检查到视频路径：" + path_mp4)
            publish_shipinhao(path_mp4)
        else:
            print("未检查到视频路径，程序终止！")
            exit()
print(get_now_time()+'全部上传完成')
exit()
2022年5月12日21:58:55
    by qiweb
技术微信：qiweb3
关注，收藏 一下
视频号：老王de日常
视频号ID:sphMlB0G4vnMbrU

公众号：QIWEB精品共享科技
bilibili 我的站功能演示 最靓的噢
自动爬取抖音个人账户全部视频，自动去水印下载，自动保存封面，全自动登录微信短视频，发布短视频， 短视频运营神器
https://www.bilibili.com/video/BV1D34y1h7M5?spm_id_from=333.999.0.0
