##################################################
#-*- coding:utf-8 -*-
# FileName: handler.py
# Author: buptxiaomiao
# Mail: buptwjh@outlook.com
# Created Time: 2017年03月07日 星期二 21时05分41秒
################################################## 
#!/usr/bin/python2.7
#Assume txt is title/patagraph/heading/list
#handler.py is to give txt HTML label

class Handler:
    """
    处理程序父类
    """
#callable()能够检查一个函数能否被调用，如果能，返回True
    def callback(self, prefix, name, *args):
#getattr()返回一个对象的属性值
#getattr(x,'foo',None)相当于foo.x
        method = getattr(self, prefix + name, None)
        if callable(method):
            return method(*args)

    def start(self, name):
        self.callback('start_', name)
    
    def end(self, name):
        self.callback('end_', name)
    
    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None:
                result = match.group(0)
            return result
        return substitution

class HTMLRender(Handler):
    """
    HTML处理程序，给文本块加相应的HTML标记
    """
    
    def start_document(self):
        print '<html><head><title>BUPTXIAOMIAO</title></head><body>'

    def end_document(self):
        print '</body></html>'

    def start_paragraph(self):
        print '<p style = "color: #444";>;'

    def end_paragraph(self):
        print '</p>'

    def start_heading(self):
        print '<h2 style = "color: #688BE5D";>'

    def end_heading(self):
        print '</h2>'

    def start_list(self):
        print '<ul style = "color: #363736;">'

    def start_listitem(self):
        print '<li>'

    def end_listitem(self):
        print '</li>'

    def end_list(self):
        print '</ul>'

    def start_title(self):
        print '<h1 style = "color: #1ABC9C">'

    def end_title(self):
        print '</h1>'

    def sub_emphasis(self, match):
        return '<em>%s<em>' %match.group(1)

    def sub_url(self, match):
        return '<a target="_blank" style="text-decoretion: none; \
                color:BC1A4B;" href="%s">%s</a>'%(match.group(1),
                 match.group(1))
    def sub_mail(self, match):
        return '<a style="text-decoration:none;color:BC1A4B;"\
                href="mailto:%s">%s</a>'%(match.group(1),match.group(1))

    def feed(self,data):
        print data

