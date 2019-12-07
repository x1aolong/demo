# -*- coding: utf-8 -*
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException, TimeoutException, NoSuchElementException
from pyquery import PyQuery as pq
import datetime
import time
import sys
import os
import re
import configparser
import pymysql
import xlrd
import csv
import importlib
importlib.reload(sys)
sys.setdefaultencoding('utf8')

# 连接数据库
conf = configparser.ConfigParser()
conf.read('./config.ini')
conn = pymysql.connect(
    host=conf.get('mysqltest', 'host'),
    user=conf.get('mysqltest', 'username'),
    password=conf.get('mysqltest', 'password'),
    database=conf.get('mysqltest', 'dbname'),
    charset=conf.get('mysqltest', 'charset')
)
db = conn.cursor()

sql = "SELECT * FROM 163_already_spider LIMIT 1"
res = db.execute(sql)
print(res)
