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
