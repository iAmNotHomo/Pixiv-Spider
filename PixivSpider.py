import requests
import os
from lxml import etree
#import json

cookie = 'first_visit_datetime_pc=2022-10-08+16:09:37; p_ab_id=7; p_ab_id_2=7; p_ab_d_id=1848536927; yuid_b=EghhZ3Y; device_token=930098cb4c6622771c91401f6d6389e6; privacy_policy_agreement=5; privacy_policy_notification=0; a_type=0; b_type=1; howto_recent_view_history=101419511; login_ever=yes; QSI_S_ZN_5hF4My7Ad6VNNAi=v:0:0; PHPSESSID=24479428_LadShC6cSwL0IY88AfRQBp8rdEz7xz9L; c_type=21; tag_view_ranking=0xsDLqCEW6~RTJMXD26Ak~5oPIfUbtd6~jH0uD88V6F~-98s6o2-Rp~Ie2c51_4Sp~_EOd7bsGyl~tgP8r-gOe_~GNcgbuT3T-~EZQqoW9r8g~3gc3uGrU1V~ZldurqefWy~KN7uxuR89w~WVrsHleeCL~faHcYIP1U0~K8_BEpmEzt~Lt-oEicbBr~ziiAzr_h04~BSlt10mdnm~HY55MqmzzQ~ETjPkL0e6r~9Gbahmahac~pnCQRVigpy~CrFcrMFJzz~azESOjmQSV~q303ip6Ui5~-sp-9oh8uv~4QveACRzn3~u8McsBs7WV~oAnKp9i65M~UKKcv4bu7d~gpglyfLkWs~WnZ0fT9WF-~2R7RYffVfj~hIbSsZ4_QS~wmxKAirQ_H~TqiZfKmSCg~K_T1KPLd2P~Bd2L9ZBE8q~AqnpayadBQ~QaiOjmwQnI~Xyw8zvsyR4~1WiF9FWDcG~eVxus64GZU~iFcW6hPGPU~qFKaG9wqf1~JChz6LAJsB~rOkjoRR5YT~F-lXdokC4U~Ged1jLxcdL~cryvQ5p2Tx~qXzcci65nj~otWaj1bQDp~8yfu_pZkcm~CkDjyRo6Vc~VTTTpeWl_Y~JflzRb7YrB~bvp7fCUKNH~4rDNkkAuj_~txZ9z5ByU7~r01unnQL0a~yREQ8PVGHN~rOnsP2Q5UN~TWrozby2UO~jk9IzfjZ6n~BtXd1-LPRH~mIBxNOpKNs~qQ77lqOSk3~ZnmOm5LdC3~_vCZ2RLsY2~q8MR54Ig90~ea63_dbx7n~aRnicZWkcZ~gXL18Qy_Kg~tAZXG3M0z-~KexWqtgzW1~qWFr0Atl5X~vzxes78G4k~_pwIgrV8TB~M2vKPRxAge~i_dZaon0j6~JTIckDtLBA~qGShmX0wgk~_GuOetFMMO~6GYRfMzuPl~-StjcwdYwv~PwDMGzD6xn~YThJ5b-nhQ~HOA5yVOSfn~KOnmT1ndWG~y8GNntYHsi~NpsIVvS-GF~U7REJ2l-CY~5WlN6qpDZj~51A0YAI8PU~4h2tbK2_VU~W6jo6IPFVp~9PI9msRK8Q~smD4GnkGMk~ZKYx1SDf_f; __cf_bm=UdkbLCuUiEDB91iOX94kOZg0nrBbkxfx_E55YZYlYhM-1665999833-0-ATZsT1cbcsjf53ild7QddaxiyoTGz00CBhLg/y3Gj+rOeAhg4ZzqCzvkOTQmZtrHu314PO49iyG8Z25guq2Hd6sTW5Yw8iSzxXpp2rGA8tY4blHisIkweRo0V6+X1fS1dCGCLxCLoVDkhstduLfxYROrrYAR1PPGOnVaz3GuZpIfqbNxk4ai3+L5BfPqeASH6w==; user_language=zh'
userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
xUserId = '24479428'
file_root_path = 'E:\\pixiv\\'


def try_get(url, headers, params):
    for i in range(10):
        try:
            data = requests.get(url=url, headers=headers, params=params)
        except Exception as e:
            print(e)
            print('retry...')
            continue
        else:
            return data


def download_single_img(pid, i, img_url, file_path):
    img_name = pid + '_p' + str(i) + '.jpg'
    if os.path.exists(file_path + img_name):  # 如果文件已存在则跳过下载
        print(pid + '_p' + str(i) + ' already exists')
    else:
        img_headers = {
            'cookie': cookie,
            'referer': 'https://www.pixiv.net/',
            'user-agent': userAgent,
            'x-user-id': xUserId
        }
        img_params = {
            'lang': 'zh'
        }
        imgData = try_get(url=img_url, headers=img_headers,
                          params=img_params).content
        img = open(file_path + img_name, 'wb')
        img.write(imgData)
        img.close()
        print(pid + '_p' + str(i) + ' saved')


def download_pid(pid, file_path, start_y, start_m, stop_y, stop_m):
    # 提取指定详情页的分p列表
    page_url = 'https://www.pixiv.net/ajax/illust/' + pid + '/pages'
    page_headers = {
        'cookie': cookie,
        'referer': 'https://www.pixiv.net/artworks/' + pid,
        'user-agent': userAgent,
        'x-user-id': xUserId
    }
    page_params = {
        'lang': 'zh'
    }
    pageData = try_get(url=page_url, headers=page_headers,
                       params=page_params).json()

    # 提取指定详情页中每张插画的原图url
    urlList = []
    for single_img in pageData['body']:
        single_img_url = single_img['urls']['original']
        # debug用，检查url字符串的截取结果，目标为截取出上传年月
        #print(single_img_url[37:41], single_img_url[42:44])
        #print(int(single_img_url[37:41])<2022, int(single_img_url[42:44])<7)
        year = int(single_img_url[37:41])
        month = int(single_img_url[42:44])
        if year > stop_y or (year == stop_y and month > stop_m):
            return [True, 0]  # 不保留终止时间以后的插画，返回true，处理本画师的下一条pid
        elif year < start_y or (year == start_y and month < start_m):
            #print('execute 1')
            return [False, 0]  # 不保留开始时间以前的插画，返回false，停止爬取本画师的插画
        else:
            #print('execute 2')
            urlList.append(single_img_url)

    # 下载指定详情页中的所有插画
    i = 0  # 循环计数器，用于文件命名以及返回值
    for img_url in urlList:
        download_single_img(pid, i, img_url, file_path)
        i += 1

    return [True, i]


def download_illustrator(uid, max, start_y, start_m, stop_y, stop_m):
    # 提取画师信息
    artist_url = 'https://www.pixiv.net/ajax/user/' + uid + '/profile/all'
    artist_headers = {
        'cookie': cookie,
        'referer': 'https://www.pixiv.net/users/' + uid,
        'user-agent': userAgent,
        'x-user-id': xUserId
    }
    artist_params = {
        'lang': 'zh'
    }
    pageData = try_get(url=artist_url, headers=artist_headers,
                       params=artist_params).json()

    # 提取画师用户名
    userName = ''
    for targetData in pageData['body']['pickup']:  # 在pageDate中搜索userName
        if 'userName' in targetData:
            userName = targetData['userName']
            break  # 跳过的语句中包括else块
    else:  # 如果pageData中没有userName，则再请求一份HTML获取userName
        artist_html_url = 'https://www.pixiv.net/users/' + uid
        artist_html_headers = {
            'user-agent': userAgent
        }
        html_pageData = try_get(url=artist_html_url,
                                headers=artist_html_headers, params={}).text
        html_encoding = etree.HTMLParser(encoding='utf-8')
        html_tree = etree.HTML(html_pageData, parser=html_encoding)
        userName = html_tree.xpath('/html/head/title/text()')[0][:-8]

    # 修改userName中的特殊字符
    userName = userName.replace('/', '-').replace('\\', '-').replace('<', '-')
    userName = userName.replace('>', '-').replace('|', '-').replace('\"', '-')
    userName = userName.replace('?', '-').replace('*', '-').replace(':', '-')

    # 指定文件保存目录
    file_path = file_root_path + uid + '-' + userName + '\\'
    if not os.path.exists(file_path):  # 如果没有则创建文件夹
        os.mkdir(file_path)
    print('file path', file_path)

    # 提取画师信息中的作品pid
    pid_List = []
    for single_pid in pageData['body']['illusts']:
        pid_List.append(single_pid)

    # 下载列表中的插画
    i = 0  # 已下载的文件的计数器
    for single_pid in pid_List[0:max]:
        response = download_pid(single_pid, file_path,
                                start_y, start_m, stop_y, stop_m)
        if response[0]:
            i += response[1]
            if i >= max:
                break
        else:  # pid对应的插画早于start_y年start_m月
            break


def get_following_list(start_offset):
    uidList = []

    url = 'https://www.pixiv.net/ajax/user/' + xUserId + '/following'
    headers = {
        'cookie': cookie,
        'referer': 'https://www.pixiv.net/users/' + xUserId + '/following',
        'user-agent': userAgent,
        'x-user-id': xUserId
    }
    offset = start_offset
    pagesize = 99
    params = {
        'offset': str(offset),
        'limit': str(pagesize),
        'rest': 'show',  # show-公开关注, hide-悄悄关注
        'tag': '',
        'acceptingRequests': '0',
        'lang': 'zh'
    }

    # 判断程序是否设置为从悄悄关注列表中开始爬取。如果offset>=公开关注列表的长度，则是。
    # 该条件等价于无法进入 while listData['body']['users'] != [] 的循环体。
    # 因为如果offset<列表长度，则提取到的第一页列表必定不是空列表。
    start_from_hide = True

    listData = try_get(url=url, headers=headers, params=params).json()
    while listData['body']['users'] != []:
        '''
        # debug用，每页json数据保存为一份文件供查看
        page = int(offset/pagesize) + 1
        print('page', page, 'on going')
        save_file = open('page'+str(page)+'.json', 'w', encoding='utf-8')
        json.dump(obj=listData, fp=save_file, ensure_ascii=False)
        '''

        start_from_hide = False  # 只要提取到了非空的公开关注列表，就不是从悄悄关注列表开始爬取。

        for user in listData['body']['users']:
            uidList.append(user['userId'])
        offset += pagesize
        params['offset'] = str(offset)  # 更新参数字典
        print('show illustrators page', int(offset/pagesize), 'done')

        listData = try_get(url=url, headers=headers, params=params).json()

    if start_from_hide:
        offset -= listData['body']['total']
    else:  # 由于刚完成公开列表的爬取，所以从头开始爬取隐藏列表
        offset = 0
    params['offset'] = str(offset)
    params['rest'] = 'hide'

    listData = try_get(url=url, headers=headers, params=params).json()
    while listData['body']['users'] != []:
        for user in listData['body']['users']:
            uidList.append(user['userId'])
        offset += pagesize
        params['offset'] = str(offset)  # 更新参数字典
        print('hide illustrators page', int(offset/pagesize), 'done')

        listData = try_get(url=url, headers=headers, params=params).json()

    return uidList


def mode1():  # 自动下载关注画师的最新的max个作品
    max = 20  # 每个画师的最大下载量
    # 若当前画师已下载插画量>=max张，则在当前pid下载完成后结束当前画师的爬取

    # 没加入(for: try)循环时，爬虫遇到网络波动立刻报错停止，因此重新启动时需要输入上次的进度。
    #offset = int(input('plz input offset: '))
    offset = 0
    uidList = get_following_list(offset)
    ListLen = len(uidList)
    i = 1  # 循环计数器
    for uid in uidList:
        download_illustrator(uid, max, 0, 0, 3000, 20)
        print('(', i, '/', ListLen, ') ', 'download has been completed', sep='')
        i += 1

    print('all download has been completed!')


def mode2():  # 下载指定画师的作品，支持通过发布日期筛选
    # 输入参数
    # 每个画师的最大下载量
    # 若当前画师已下载插画量>=max张，则在当前pid下载完成后结束当前画师的爬取
    max = int(input(
        'plz input the max img num of single illustrator, 0 represents no limit: '))
    if max <= 0:
        max = 999
    # 画师数量
    num = int(input('plz input the num(>=1) of wanted illustrators: '))
    if num < 1:
        num = 1

    uidList = []
    start_y = []
    start_m = []
    stop_y = []
    stop_m = []

    for i in range(num):
        print('(', i+1, '/', num, ') ', sep='', end='')
        uidList.append(input('plz input illustrator uid: '))

        # 起始时间
        print('(', i+1, '/', num, ') ', sep='', end='')
        if bool(int(input('set earliest date? input 0/1: '))):
            start_y.append(
                int(input('plz input the earliest year of wanted illustrations: ')))
            start_m.append(
                int(input('plz input the earliest month of wanted illustrations: ')))
        else:
            start_y.append(0)
            start_m.append(0)

        # 终止时间
        print('(', i+1, '/', num, ') ', sep='', end='')
        if bool(int(input('set latest date? input 0/1: '))):
            stop_y.append(
                int(input('plz input the latest year of wanted illustrations: ')))
            stop_m.append(
                int(input('plz input the latest month of wanted illustrations: ')))
        else:
            stop_y.append(3000)
            stop_m.append(20)

    # 下载
    print('download has been started...')
    for i in range(num):
        #print(uid[i], start_y[i], start_m[i], stop_y[i], stop_m[i])
        download_illustrator(
            uidList[i], max, start_y[i], start_m[i], stop_y[i], stop_m[i])  # 起止时间为闭区间
        print('(', i+1, '/', num, ') ', 'download has been completed', sep='')

    print('all download has been completed!')


def mode3():  # 下载最近更新的若干个pid
    pagesize = 60  # 更新列表中每页有60张画
    num = int(input('plz input download num: '))
    imgList = []

    latest_url = 'https://www.pixiv.net/ajax/follow_latest/illust'
    latest_headers = {
        'cookie': cookie,
        'referer': 'https://www.pixiv.net/bookmark_new_illust.php',
        'user-agent': userAgent,
        'x-user-id': xUserId
    }
    page = 1
    latest_params = {
        'p': str(page),
        'mode': 'all',
        'lang': 'zh'
    }

    i = num
    while i > 0:
        i -= pagesize
        listData = try_get(
            url=latest_url, headers=latest_headers, params=latest_params).json()
        imgList += listData['body']['thumbnails']['illust']
        page += 1
        latest_params['p'] = str(page)

    for i in range(num):
        imgData = imgList[i]

        userName = imgData['userName']
        # 修改userName中的特殊字符
        userName = userName.replace(
            '/', '-').replace('\\', '-').replace('<', '-')
        userName = userName.replace(
            '>', '-').replace('|', '-').replace('\"', '-')
        userName = userName.replace(
            '?', '-').replace('*', '-').replace(':', '-')

        pid = imgData['id']

        file_path = file_root_path + imgData['userId'] + '-' + userName + '\\'
        if not os.path.exists(file_path):  # 如果没有则创建文件夹
            os.mkdir(file_path)

        print(file_path)
        download_pid(pid, file_path, 0, 0, 3000, 20)
        print('(', i+1, '/', num, ') ', 'download has been completed', sep='')

    print('all download has been completed!')


if __name__ == '__main__':
    print('mode select:')
    print('1: download the latest 20(default) imgs of every illustrator in your following list')
    print('2: select several illustrators and download their imgs with personal limits')
    print('3: download the latest several imgs in your following list')
    mode = int(input('plz input running mode: '))
    if mode == 1:
        mode1()
    elif mode == 2:
        mode2()
    elif mode == 3:
        mode3()
    else:
        print('invalid mode code.')
