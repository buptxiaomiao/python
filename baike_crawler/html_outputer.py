##################################################
#-*- coding:utf-8 -*-
# FileName: html_outputer.py
# Author: buptxiaomiao
# Mail: buptwjh@outlook.com
# Created Time: 2017年03月22日 星期三 21时09分09秒
##################################################
#!/usr/bin/python2.7

class HtmlOutputer(object):
    """"""
    def __init__(self):
        self.datas = []

    def collect_data(self,data):
        if data is None:
            return None
        else:
            self.datas.append(data)

    def output_html(self):
        with open('output.html', 'w') as f:
            f.write('<html><head><meta charset="UTF-8"</head>')
            f.write('<body>')
            f.write('<table>')

            for data in self.datas:
                f.write("<tr>")
                f.write("<td>%s</td>"%data['url'])
                f.write("<td>%s</td>"%data['title'].encode('utf-8'))
                f.write("<td>%s</td>"%data['summary'].encode('utf-8')) 
                f.write("</tr>")
            f.write("</table>")
            f.write("</body>")
            f.write("/html")
