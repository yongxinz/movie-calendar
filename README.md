# movie-calendar


## 首页

![](http://ww1.sinaimg.cn/large/0061a0TTly1g50tdf4u23j30ad0iiab4.jpg)

## 环境

系统版本：CentOS 7.6，Python 版本： python 3.6 <br>
后端使用：Django + restframework，具体版本信息见 requestments.txt <br>
小程序基础库版本 1.5.3

## 安装

### 安装 python3

分两种方式：RPM 包方式安装和源码编译安装，下面分别进行介绍：

#### RPM 包方式：

详细可看[官方文档](https://ius.io/GettingStarted/#install-via-automation)，具体命令如下：
>yum -y install https://centos7.iuscommunity.org/ius-release.rpm

>yum makecache

>yum install python36u

>yum -y install python36u-pip

>yum -y install python36u-devel

执行完以上命令之后即可正常使用。

#### 源码编译：

从[Python 官网](https://www.python.org/downloads/)下载源码包。

>yum -y install wget gcc make  zlib-devel readline-devel  bzip2-devel ncurses-devel sqlite-devel gdbm-devel xz-devel tk-devel openssl-devel

>wget https://www.python.org/ftp/python/3.6.1/Python-3.6.1.tar.xz

>xz -d Python-3.6.1.tar.xz

>tar -xvf Python-3.6.1.tar

>cd Python-3.6.1

>./configure --prefix=/usr/local/python3.6 --enable-optimizations

>make

>make install

>ln -s /usr/local/python3.6/bin/python3 /usr/bin/python3

### 新建虚拟环境

>pip install virtualenv 

>pip install virtualenvwrapper
 
然后编辑 .bash_profile 文件，添加下面三行：

>VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.6 

>export WORKON_HOME=~/.virtualenvs 

>source /usr/bin/virtualenvwrapper.sh

然后执行 source .bash_profile，接下来就可以创建虚拟环境了。
>mkvirtualenv movie --python=python3

### 安装依赖包
>cd movie <br>
>pip install -r requestments.txt

### 安装 PostgreSQL

>yum -y install postgresql-server postgresql-contrib

>postgresql-setup initdb

>systemctl start postgresql

>systemctl enable postgresql

切换用户，并且新建数据库：

>su - postgres

> psql

> create database movie;

### 初始化表
>python manage.py migrate

### 初始化数据
#### 抓取豆瓣 top250 的电影数据
>python manage.py douban_top250

#### 抓取热映内容
>python manage.py in_theaters

### Run，并运行小程序
>python manage.py runserver 0.0.0.0:8820

## 抢先体验

![一个电影日历小程序码](http://ww1.sinaimg.cn/large/0061a0TTly1g50t5jszi9j3076076js8.jpg)
