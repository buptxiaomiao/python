#########################################################################
#-*- coding:utf-8 -*-
# File Name: partial-ex.py
# Author: buptxiaomiao
# mail: buptxiaomiao@outlook.com
# Created Time: 2016年03月21日 星期一 22时10分38秒
#########################################################################
#!/usr/bin/env python2.7

from functools import partial
import Tkinter

root = Tkinter.Tk()
mybutton = partial(Tkinter.Button,root,fg='write',bf='blue')
b1 = mybutton(text = 'Button 1')
b2 = mybutton(text = 'Button 2')
qb = mybutton(text = 'QUIT',bg = 'red',command = root.quit)
b1.pack()
b2.pack()
qb.pack(fill = Tkinter.X,expand = True)
root.title = ('PFAs!')
root.mainloop()
