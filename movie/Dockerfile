FROM python:3.6.8
LABEL movie=1.0

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /movie
COPY ./requirements.txt /movie

WORKDIR /movie

RUN sed -i "s/archive.ubuntu./mirrors.aliyun./g" /etc/apt/sources.list
RUN sed -i "s/deb.debian.org/mirrors.aliyun.com/g" /etc/apt/sources.list

RUN apt-get clean && apt-get -y update && \
    apt-get -y install libsasl2-dev python-dev libldap2-dev libssl-dev libsnmp-dev
RUN pip3 install --index-url https://mirrors.aliyun.com/pypi/simple/ --no-cache-dir -r requirements.txt

COPY ./* /movie/
