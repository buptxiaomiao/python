##################################################
#-*- coding:utf-8 -*-
# FileName: crawl_main.py
# Author: buptxiaomiao
# Mail: buptwjh@outlook.com
# Created Time: 2017年03月22日 星期三 21时29分30秒
##################################################
#!/usr/bin/python2.7

import url_manager
import html_downloader
import html_parser
import html_outputer
import time

class CrawlerMain(object):
    """
        爬虫调度器
    """
    def __init__(self):
        """
            初始化
            1.URL管理器
            2.网页下载器
            3.网页解析器
            4.提取价值数据
        """
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self, root_url):
        """
            调度器爬虫入口函数
        """
        self.urls.add_new_url(root_url)#入口
        count = 1
        try:
            while self.urls.has_new_url():#有待爬取URL
                new_url = self.urls.get_new_url()#取新URL
                content = self.downloader.download(new_url)#下载网页内容
                #解析下载的网页1.提取新URL 2.解析网页内容
                new_urls, new_data = self.parser.parse(new_url, content)
                self.urls.add_new_urls(new_urls)#新URL加入URL管理器
                self.outputer.collect_data(new_data)#价值数据-->收集数据
                print count, new_url
                if count == 20:
                    break
                count += 1
        except Exception, e:#防止网页为空or其他异常使程序崩溃
            print e
            print "download fail"
        self.outputer.output_html()#网页输出

if __name__ == "__main__":
    start = time.time()
    root_url = "http://baike.baidu.com/item/Python"
    object_spider = CrawlerMain()
    object_spider.crawl(root_url)
    end = time.time()
    print "cost all time: %s"%(end - start)
