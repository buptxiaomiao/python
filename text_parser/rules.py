##################################################
#-*- coding:utf-8 -*-
# FileName: rules.py
# Author: buptxiaomiao
# Mail: buptwjh@outlook.com
# Created Time: 2017年03月07日 星期二 21时35分50秒
################################################## 
#!/usr/bin/python2.7
#rules.py is to judge which label should be attached to the block

class Rule:
    """
    规则父类
    """
    
    def action(self, block, handler):
        """
        加标记
        """
        handler.start(self.type)
        handler.feed(block)
        handler.end(self.type)
        return True

class HeadingRule(Rule):
    """
    一号标题规则
    """
    type = 'heading'
    def condition(self, block):
        """
        判断文本块是否符合规则
        """

        return not '\n' in block and len(block) <= 70 and not block[-1] == ':' 
class TitleRule(HeadingRUle):
    """
    二号标题规则
    """
    type = 'title'
    first = True
    
    def condition(self, block):
        if not self.first:
            return False
        self.first = False
        return HeadingRule.condition(self,block);

class ListItemRule(Rule):
    """
    列表项规则
    """
