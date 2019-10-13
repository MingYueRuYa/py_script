# 收集weibo某段时间的数据
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import os

def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    driver.start_client()
    return driver

def q(st, et):
    return f'is_ori=1&key_word=&start_time={st}&and_time={et}&is_search=1&is_searchadv=1#_0'