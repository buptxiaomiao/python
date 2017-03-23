##################################################
#-*- coding:utf-8 -*-
# FileName: html_outputer.py
# Author: buptxiaomiao
# Mail: buptwjh@outlook.com
# Created Time: 2017年03月22日 星期三 21时09分09秒
##################################################
#!/usr/bin/python2.7

class HtmlOutputer(object):
    """
        1.收集价值数据
        2.将价值数据输出到HTML文件
    """
    def __init__(self):
        self.datas = []#保存收集的数据对象

    def collect_data(self,data):
        """
            收集价值数据
        """
        if data is None:
            return None
        else:
            self.datas.append(data)#将价值数据添加到类中

    def output_html(self):
        """
            将价值数据输出
        """
        #with open('***','*') as f:
        with open('output.html', 'w') as f:
            f.write('<html><head><meta charset="UTF-8"></head>')
            f.write('<body>')
            f.write('<table>')

            #价值数据输出到表格
            for data in self.datas:
                f.write("<tr>")
                f.write("<td>%s</td>"%data['url'])
                #python 写入文件ASCII码，将数据转换成utf-8编码
                f.write("<td>%s</td>"%data['title'].encode('utf-8'))
                f.write("<td>%s</td>"%data['summary'].encode('utf-8')) 
                f.write("</tr>")
            f.write("</table>")
            f.write("</body>")
            f.write("/html")
