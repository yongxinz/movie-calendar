# movie-calendar


## 首页

![](http://ohl540wt2.bkt.clouddn.com/1510709943520.jpg)

## 环境

Python 版本为 python3.6，后端使用：Django + restframework <br>
小程序基础库版本 1.5.3

## 安装

1、新建虚拟环境
>mkvirtualenv movie --python=python3

2、安装依赖包
>cd movie <br>
>pip install -r requestments.txt

3、初始化表
>python manage.py migrate

4、抓取豆瓣 top250 的电影数据
>python manage.py douban_top250

5、Run，并运行小程序
>python manage.py runserver 0.0.0.0:8810

## 抢先体验

![一个电影日历小程序码](http://ohl540wt2.bkt.clouddn.com/movie-calendar.jpg)
