import requests
import json
import csv

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
                        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}

# 通过浏览器F12找到API里的参数
shown_offset = [1525959315000002]


# 访问 API 地址，获取数据
def get_info(url):
    global shown_offset
    req = requests.get(url,headers=header)
    content = req.json()
    shown_offset.append(content['shown_offset'])

    info = []
    for item in content['articles']:
        lst = []
        try:
            lst.append(item['title'])
            lst.append(item['views'])
            lst.append(item['user_name'])
            info.append(lst)
        except Exception as e:
            print(e)
            continue

    return info


# 保存到文件
def save(lst):

    with open('csdn.csv','w',encoding='utf-8')as f:
        writer = csv.writer(f)
        writer.writerow(['标题','浏览量','作者'])
        for i in lst:
            writer.writerow(i)


# 主函数
def main():
    global shown_offset
    url = 'https://www.csdn.net/api/articles?type=more&category=newarticles&shown_offset={}'


    # 获取前 3 个时间戳
    data_lst = []
    for i in range(3):
        offset = shown_offset.pop()
        t_url = url.format(offset)
        print('正在获取:',t_url)
        lst_info = get_info(t_url)
        data_lst.extend(lst_info)
    save(data_lst)

if __name__ == '__main__':
    main()