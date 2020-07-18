# coding:utf-8

import re
import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand

from top.models import Top


class Command(BaseCommand):
    help = 'get douban movie top250'

    def handle(self, *args, **options):
        num = 0
        while num <= 250:
            user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
            headers = {}
            headers['user-agent'] = user_agent
            url = 'https://movie.douban.com/top250?start=' + str(num) + '&filter='
            num += 25
            '''
            利用循环实现翻页并获取网页内容
            '''
            response = requests.get(url, headers=headers)
            print(response)
            soup = BeautifulSoup(response.text, 'lxml')
            movies = soup.find_all('div', class_="item")

            for info in movies:
                detail = info.select('.bd p')[0].text.strip().split('\n')
                detail_ = detail[0].split(':')

                directors = ''
                casts = ''
                if len(detail_) == 3:
                    directors = detail_[1].split('主演')[0].strip()
                    casts = detail_[2].strip()

                if directors == '' or casts == '':
                    continue

                # 获得电影的中文名
                title = info.find('span', class_='title').text  # find()只找到一个，结果以树结构返回

                tmp = info.find('div', class_='star')
                tmp = re.search('rating(\S+?)-t', str(tmp))
                stars = re.findall('\d+', str(tmp))[2]
                if int(stars) <= 5:
                    stars += '0'

                # 获得电影在豆瓣中的链接
                link = info.find('a').get('href')

                subject = re.findall('\d+', link)

                images = info.find('img').get('src')

                year = detail[1].split('/')[0].strip()

                # 找到评分以及评价人数
                rating = info.find(class_='rating_num').text

                # 获得一句话评价
                comment_one = info.find('span', class_='inq')
                if comment_one is None:
                    comment = u' '
                else:
                    comment = comment_one.text

                print(subject[0], title, link, rating, comment, directors, casts, year, images, stars)

                Top.objects.update_or_create(subject=subject[0], defaults={'title': title, 'link': link,
                                                                           'rating': rating, 'comment': comment,
                                                                           'year': year, 'directors': directors,
                                                                           'casts': casts, 'images': images,
                                                                           'stars': int(stars)})
