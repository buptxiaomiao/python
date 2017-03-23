##################################################
#-*- coding:utf-8 -*-
# FileName: url_manager.py
# Author: buptxiaomiao
# Mail: buptwjh@outlook.com
# Created Time: 2017年03月22日 星期三 16时34分47秒
##################################################
#!/usr/bin/python2.7


#URL管理器实现
#1.内存 
#   待爬取URL集合:set()  
#   已爬取URL集合:set()
#2.关系数据库
#   urls(url, is_crawled)
#3.缓存数据库redis
#   待爬取URL集合:set
#   已爬取URL集合:set

class UrlManager(object):
    """
        URL管理器
        防止重复抓取，防止循环抓取
            1.添加新URL(s),判断是否在容器中
            2.是否有待爬取URL
            3.取待爬URL，并添加到已爬中
    """
    def __init__(self):
        """将待爬取url、已爬取url存到内存set()中"""
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
