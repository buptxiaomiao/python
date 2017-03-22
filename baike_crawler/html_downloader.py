##################################################
#-*- coding:utf-8 -*-
# FileName: html_downloader.py
# Author: buptxiaomiao
# Mail: buptwjh@outlook.com
# Created Time: 2017年03月22日 星期三 16时45分10秒
################################################## 
#!/usr/bin/python2.7
import urllib2

class HtmlDownloader(object):
    def download(self,url):
        headers = ("User-Agent":"Mozilla/5.0",\
                    "Referer":"http://www.baidu.com")
        req = urllib2.Request(url,headers = headers)
        response = urllib2.urlopen(req)

        if (response.getcode() == 200):
            return response.read()
        else:
            return None
    
