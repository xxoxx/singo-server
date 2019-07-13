# singo

> singo运维平台后台
前端项目地址: https://github.com/lemon1912/singo-web

# singo功能
```
用户管理、LDAP管理、资产管理、工单系统、权限管理、项目部署、salt管理
```
# 开发语言与框架：
```
该项目是采用前后端分离开发
开发语言:python 3.6
后台框架:django 1.11 + djangorestframework 3.9.0
异步框架: apscheduler 3.5.3 + redis
已对接工具: salt、jenkins、gitlab、ldap
```

# 安装准备


## 升级系统
```
$ sudo add-apt-repository universe
$ sudo apt-get update
$ sudo apt-get -y upgrade
```

## 安装pip软件管理工具
```
$ sudo apt-get install -y python3-pip
```

## 安装开发工具
```
$ sudo apt-get install build-essential libssl-dev libffi-dev python-dev
```

## 安装虚拟化工具
```
$ sudo apt-get install -y python3-venv
```


## 创建虚拟化环境
```
$ python3 -m venv project_env
```

## 切换虚拟化环境
```
$ source project_env/bin/activate
$ deactivate
```

# 安装数据库

## 安装MariaDB 10.3
```
$ sudo apt-get install software-properties-common
$ sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xF1656F24C74CD1D8
$ sudo add-apt-repository 'deb [arch=amd64] http://mirror.zol.co.zw/mariadb/repo/10.3/ubuntu bionic main'
$ sudo apt -y install mariadb-server mariadb-client libmysqlclient-dev
```

## 创建数据库
```
$ mysql -uroot -p
\> create database devops default charset 'utf8';
\> grant all on devops.* to 'devops'@'127.0.0.1' identified by 'lemon1912';
\> flush privileges;
```

## 其他安装
```
$ sudo apt install redis-server libmysqlclient-dev git
$ sudo systemctl enable redis-server.service
```

# 安装项目


## 克隆项目
```
$ cd /opt
$ sudo git ***
```

## 导入数据
```
$ cd /opt/devops-server
$ mysql -uroot -p devops < requirements/devops.sql
```

## 安装依赖
```
$ cd /opt/devops-server
$ pip install -r requirements/requirements.txt
```

##启动项目
```
$ python manage.py runserver 127.0.0.1:8418
```

## 后续
```
此项目目前仅作前后端项目分离及运维平台建设的参考,后期会陆续完善及加入更多功能
```

