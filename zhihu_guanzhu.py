# 自动关注粉丝

from selenium import webdriver
import time

def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    return driver

def find_stranger():
    btn_sel = 'div.ContentItem-extra > button.Button--blue'
    elems = driver.find_element_by_css_selector(btn_sel)
    return elems

while True:
    url = 'https://www.zhihu.com'
    # 需替换成你的知乎url，点击【我的主页】→【关注者】可进入该页面
    follwer_url = 'https://www.zhihu.com/people/ha-yoo/followers'
    driver = start_chrome()
    driver.get(url)
    if not driver.get_cookies():
        # push()
        pass
    # wait login
    time.sleep(20)
    driver.get(follwer_url)
    # wait for page loading and users
    time.sleep(6)
    strangers = find_stranger()
    for s in strangers:
        s.click()
        time.sleep(3)
    print('Done')