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

class HtmlParser(object):

    def parse(self, page_url, content):
        soup = BeautifulSoup(content, 'html.parser',\
              from_encoding = 'utf-8')
        urls = self._get_new_urls(page_url, soup)
        data = self._get_new_data(page_url, soip)
        return urls, data

    def _get_new_urls(self, page_url, soup):
        new_urls = []
        links = soup.find_all('a',href = re.compile("view/\d+\.(html|htm)"))
        for link in links:
            url = link['href']
            url = urlparse.urljoin(page_url,url)
            new_urls.append(url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        data = {}
        title_node = soup.find('dd',
                    class_ = "lemmaWgt-lemmaTitle-title").find('h1')
        data['title'] = title_node.get_text()
        #<div class="lemma-summary" label -module="lemmaSummary">
        summary_node = soup.find('div',class_ = "lemma-summary")
        data['summary'] = summary_node.get_text()
        data['url'] = page_url
        return data







