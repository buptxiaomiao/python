##################################################
#-*- coding:utf-8 -*-
# FileName: html_downloader.py
# Author: buptxiaomiao
# Mail: buptwjh@outlook.com
# Created Time: 2017年03月22日 星期三 16时45分10秒
################################################## 
#!/usr/bin/python2.7
import urllib2

#用urllib2 下载网页（有3种方式第二种）
#用Request下载网页

class HtmlDownloader(object):
    def download(self,url):
        """下载器"""
        #包装头
        headers = {"User-Agent":"Mozilla/5.0",\
                    "Referer":"http://www.baidu.com"}
        req = urllib2.Request(url, headers = headers)#添加头
        response = urllib2.urlopen(req)

        if (response.getcode() == 200):#获取状态码，如果是200,读取
            return response.read()
        else:
            return None
