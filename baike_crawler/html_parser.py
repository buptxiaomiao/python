##################################################
#-*- coding:utf-8 -*-
# FileName: html_parser.py
# Author: buptxiaomiao
# Mail: buptwjh@outlook.com
# Created Time: 2017年03月22日 星期三 16时51分15秒
################################################## 
#!/usr/bin/python2.7

from bs4 import BeautifulSoup
import urlparse,re
#网页解析器1.re 2.html.parser 3.BeautifulSoup 4.lxml

class HtmlParser(object):
    """网页解析器"""

    def parse(self, page_url, content):
        """
            用bs解析网页内容
        """
        #1.实例化bs对象
        soup = BeautifulSoup(
                content, #要解析的内容
                'html.parser',#Bs有2种解析器，html.parser & lxml
                from_encoding = 'utf-8')#网页编码
        urls = self._get_new_urls(page_url, soup)#提取的新URL
        data = self._get_new_data(page_url, soup)#提取的价值数据
        return urls, data

    def _get_new_urls(self, page_url, soup):
        """
            从网页中提取新URL
        """
        new_urls = []
        #2.从bs对象中提取节点
        links = soup.find_all('a',\
                href = re.compile(r"item/\w+\.?(html|htm)?"))#可以用re
        for link in links:
            url = link['href']#不完整url
            url = urlparse.urljoin(page_url,url)#拼接URL
            new_urls.append(url)#新rul添加到urls[]中返回
        return new_urls

    def _get_new_data(self, page_url, soup):
        """
            从网页中提取价值数据
        """
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        data = {}
        #2.从bs对象中提取价值
        title_node = soup.find('dd',
                    class_ = "lemmaWgt-lemmaTitle-title").find('h1')
        data['title'] = title_node.get_text()#获取节点内容
        #<div class="lemma-summary" label -module="lemmaSummary">
        summary_node = soup.find('div',class_ = "lemma-summary")
        data['summary'] = summary_node.get_text()#获取节点内容
        data['url'] = page_url#获取节点内容
        return data
