#coding=utf-8

# 监听某条weibo的转发数，点赞数

from selenium import webdriver
import time

url = 'https://weibo.com/5869525717/G2VASlH1o?from=page_1005055869525717_profile&wvr=6&mod=weibotime&type=comment'

def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    driver.start_client()
    return driver

def find_info():
    #css selector
    sel = 'span > span.line.S_line1 > span > em:nth-child(2)'
    elems = driver.find_elements_by_css_selector(sel)
    return [int(el.text) for el in elems[1:]]

while True:
    driver = start_chrome()
    driver.get(url)
    time.sleep(30)
    info = find_info()
    rep,comm,like = info
    if rep > 3000:
        print('你关注的微博转发量已经过：' + str(rep))
        break
    else:
        print('Not hanppening')
    time.sleep(1200)
print('Done!')