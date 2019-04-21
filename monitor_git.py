#coding=utf-8

from datetime import datetime
import requests

import sys


def get_infolist():
    api     = 'https://api.github.com/search/repositories?q='
    query   = 'topic:crawler+language:python+'
    when    = 'created:2017-07-01'
    full_url = api + query + when
    print(full_url)
    r = requests.get(full_url)
    return r.json()['items']

#info_list = get_infolist()  
#for info in info_list:
#    str_template = 'name={name}, htmlurl={htmlurl}, message={message}'
#    print(str_template.format(name=info['name'], htmlurl=info['html_url'], message=info['description']))

print('中文')
