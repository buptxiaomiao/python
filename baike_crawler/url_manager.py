##################################################
#-*- coding:utf-8 -*-
# FileName: url_manager.py
# Author: buptxiaomiao
# Mail: buptwjh@outlook.com
# Created Time: 2017年03月22日 星期三 16时34分47秒
##################################################
#!/usr/bin/python2.7
class UrlManager(object):
    def __init__(self):
        self.urls = set()
        self.visited = set()

    def add_new_url(self, url):
        if url is None:
            return None
        if url not in self.visited:
            self.urls.add(url)

    def add_new_urls(self, urls):
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.urls) != 0

    def get_new_url(self):
        new_url = self.urls.pop()
        self.visited.add(new_url)
        return new_url
