##################################################
#-*- coding:utf-8 -*-
# FileName: huffman_code.py
# Author: buptxiaomiao
# Mail: buptwjh@outlook.com
# Created Time: 2017年03月16日 星期四 18时11分52秒
################################################## 
#!/usr/bin/python2.7
import six
import sys

class HuffNode(object):
    """
        定义一个叶节点，中间节点的父类
        1.获取节点权重
        2.是否为子节点
    """
    def get_weight(self):
        raise NotImplementedError(
            "The Abstract Node Class doesn't define 'get_weight()'")

    def isleaf(self):
        raise NotImolementedError(
            "The Abstract Node Class doesn't define 'isleaf()")


class LeafNode(HuffNode):
    """
        叶节点类
        1.字符值
        2.权重
        3.返回是叶节点
    """
    def __init__(self, value = 0, freq = 0):
    #叶节点构造时需要提供值+频次
        super(LeafNode, self).__init__()
        self.value = value
        self.weight = freq

    def isleaf(self):
        return True

    def get_weight(self):
        return self.weight
    
    def get_value(self):
        """获取叶节点的字符值"""
        return self.value


class MidNode(HuffNode):
    """
        中间节点类
        1.返回非叶节点
        2.权重
        3.左孩子
        4.右孩子
    """
    def __init__(self, left_child = None, right_child = None):
    #MidNode构造时，需要提供左孩子，右孩子
        super(MidNode, self).__init__()
        self.weight = left_child.get_weight() + right_child.get_weight()
        #中间节点的权重 = 左孩子 + 右孩子
        self.left_child = left_child
        self.right_child = right_child

    def isleaf(self):
        return False

    def get_weight(self):
        return self.weight
    
    def get_left(self):
        return self.left_child

    def get_right(self):
        return self.right_child

class HuffTree(object):
    """
        哈夫曼树
    """
    def __init__(self, flag, value = 0, freq = 0, \
                left_tree = None, right_tree = None):
        #flag = 0 --> 只包含一个叶节点的哈夫曼树
        #flag = 1 --> 多于一个叶节点的哈夫曼树
        super(HuffTree, self).__init__()
        if flag == 0:
            self.root = LeafNode(value, freq)
        else:
            self.root = MidNode(left_tree.get_root(), right_tree.get_root())
    
    def get_root(self):
        return self.root

    def get_weight(self):
        return self.root.get_weight()

    def traverse_huffman_tree(self, root, code, char_freq):
        """
            利用递归遍历huffman_tree,并且以此方式得到每个字符的huffman编码
            保存在字典char_freq中
        """
        if root.isleaf():
            char_freq[root.get_value()] = code
            print "it = %d%c and freq = %d code = %s"%(root.get_value(), \
                chr(root.get_value()), root.get_weight(), code)
            return None
        else:
            self.traverse_huffman_tree(root.get_left(), code+'0', char_freq)
            self.traverse_huffman_tree(root.get_right(), code+'1', char_freq)

def buildHuffmanTree(list_hufftrees):
    """
        构造haffman树
    """
    while len(list_hufftrees) > 1:
        #1. 按照weight对huffman树进行从小到大排序
        list_hufftrees.sort(key = lambda x: x.get_weight())
        #2. 挑出weight最小的两个huffman编码树
        print len(list_hufftrees)
        temp1 = list_hufftrees[0]
        temp2 = list_hufftrees[1]
        list_huffmantrees = list_hufftrees[2:]
        #3. 构造一个新的huffman树
        newed_hufftree = HuffTree(1, 0, 0, temp1, temp2)
        #4. 新树放入编码树list中
        list_hufftrees.append(newed_hufftree)
    return list_hufftrees[0]


if __name__ == '__main__':
    #获取用户输入
    if len(sys.argv) != 2:
        print "Please input inputfilename"
        exit(0)
    else:
        INPUTFILE = sys.argv[1]
    
    f = open(INPUTFILE, 'rb')
    filedata = f.read()
    filesize = f.tell()
    char_freq = {}
    for x in range(filesize):
        tem = six.byte2int(filedata[x])
        if tem in char_freq.keys():
            char_freq[tem] = char_freq[tem] + 1
        else:
            char_freq[tem] = 1
    for tem in char_freq.keys():
        print tem, ':', char_freq[tem]

    list_hufftrees = []
    for x in char_freq.keys():
        tem = HuffTree(0, x, char_freq[x], None, None)
        list_hufftrees.append(tem)

    tem = buildHuffmanTree(list_hufftrees)
    tem.traverse_huffman_tree(tem.get_root(), '', char_freq)
