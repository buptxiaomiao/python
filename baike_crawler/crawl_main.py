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
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        self.urls.add_new_url(root_url)
        count = 1
        try:
            while self.urls.has_new_url():
                new_url = self.urls.get_new_url()
                print '1'
                content = self.downloader.download(new_url)
                print '2'
                new_urls, new_data = self.parser.parse(new_url, content)
                print '3'
                self.urls.add_new_urls(new_urls)
                print '4'
                self.outputer.collect_data(new_data)
                print count, new_url
                if count > 20:
                    break
                count += 1
        except Exception, e:
            print e
            print "download fail"
        self.outputer.output_html()

if __name__ == "__main__":
    start = time.time()
    root_url = "http://baike.baidu.com/view/21087.htm"
    object_spider = CrawlerMain()
    object_spider.craw(root_url)
    end = time.time()
    print "cost all time: %s"%(end - start)
