##################################################
#-*- coding:utf-8 -*-
# FileName: util.py
# Author: buptxiaomiao
# Mail: buptwjh@outlook.com
# Created Time: 2017年03月07日 星期二 20时44分44秒
################################################## 
#!/usr/bin/python2.7
#parser txt to some blocks

def lines(file):
    "'
    生成器，在文本最后加一行空行
    '"
    for line in file:
        yield line
    yield '\n'

def blocks(file):
    "'
    生成器，生成单独的文本块
    '"
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()#''.join(list)把list元素用''拼接
                                #str.strip(),去掉前后的空格和换行符
                                #str.strip('me'),去掉前后的me
            block = []
            

            
    
