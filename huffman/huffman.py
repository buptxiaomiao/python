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
        self.left_child = left_child
        self.right_child = right_child
        self.weight = left_child.get_weight() + right_child.get_weight()
        #中间节点的权重 = 左孩子 + 右孩子

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
        temp1 = list_hufftrees[0]
        temp2 = list_hufftrees[1]
        list_hufftrees = list_hufftrees[2:]

        #3. 构造一个新的huffman树
        newed_hufftree = HuffTree(1, 0, 0, temp1, temp2)

        #4. 新树放入编码树list中
        list_hufftrees.append(newed_hufftree)
    return list_hufftrees[0]

def compress(inputfilename, outputfilename):
    """
        压缩文件
        inputfilename:被压缩文件
        outputfilename:压缩后的文件
    """
    f = open(inputfilename, 'rb')
    filedata = f.read()
    filesize = f.tell()
    char_freq = {}
    for x in range(filesize):
        tem = six.byte2int(filedata[x])
        if tem in char_freq.keys():
            char_freq[tem] += 1
        else:
            char_freq[tem] = 1

    for tem in char_freq.keys():
        print tem, ':', char_freq[tem]
    
    list_hufftrees = []
    for x in char_freq.keys():
        tem = HuffTree(0, x, char_freq[x], None, None)
        list_hufftrees.append(tem)
    
    length = len(char_freq.keys())  
    output = open(outputfilename, 'wb')

    a4 = length & 255
    length = length >> 8
    a3 = length & 255
    length = length >> 8 
    a2 = length & 255
    length = length >> 8
    a1 = length & 255
    output.write(six.int2byte(a1))
    output.write(six.int2byte(a2))
    output.write(six.int2byte(a3))
    output.write(six.int2byte(a4))

    for x in char_freq.keys():
        output.write(six.int2byte(x))
    
        temp = char_freq[x]
        a4 = temp & 255
        temp = temp >> 8
        a3= temp & 255
        temp = temp >> 8
        a2 = temp & 255
        temp = temp >> 8
        a1 = temp & 255
        output.write(six.int2byte(a1))
        output.write(six.int2byte(a2))
        output.write(six.int2byte(a3))
        output.write(six.int2byte(a4))

    tem = buildHuffmanTree(list_hufftrees)
    tem.traverse_huffman_tree(tem.get_root(), '', char_freq)

    code = ''
    for i in range(filesize):
        key = six.byte2int(filedata[i])
        code = code + char_freq[key]
        out = 0
        while len(code) > 8:
            for x in range(8):
                out = out << 1
                if code[x] == '1':
                    out = out|1
            code = code[8:]
            output.write(six.int2byte(out))
            out = 0

    output.write(six.int2byte(len(code)))
    out = 0
    for i in range(len(code)): 
        out = out << 1
        if code[i] == '1':
            out = out|1
    for i in range(8 - len(code)):
        out = out << 1

    output.write(six.int2byte(out))
    output.close()

def decompress(inputfilename, outputfilename):
    """
        解压缩文件
        inputfilename:被压缩的文件
        outputfilename:解压缩出来的文件
    """
    f = open(inputfilename, 'rb')
    filedata = f.read()
    filesize = f.tell()
   
    a1 = six.byte2int(filedata[0])
    a2 = six.byte2int(filedata[1])
    a3 = six.byte2int(filedata[2])
    a4 = six.byte2int(filedata[3])
    
    j = 0
    j = j|a1
    j = j<<8
    j = j|a2
    j = j<<8
    j = j|a3
    j = j<<8
    j = j|a4

    leaf_node_size = j

    char_freq = {}
    for i in range(leaf_node_size):
        c = six.byte2int(filedata[4+i*5+0])
        
        a1 = six.byte2int(filedata[4+i*5+1])
        a2 = six.byte2int(filedata[4+i*5+2])
        a3 = six.byte2int(filedata[4+i*5+3])
        a4 = six.byte2int(filedata[4+i*5+4])
        j = 0
        j = j|a1
        j = j<<8
        j = j|a2
        j = j<<8
        j = j|a3
        j = j<<8
        j = j|a4
        print c,j
        char_freq[c] = j

    list_hufftrees = []
    for x in char_freq.keys():
        tem = HuffTree(0, x, char_freq[x], None, None)
        list_hufftrees.append(tem)

    tem = buildHuffmanTree(list_hufftrees)
    tem.traverse_huffman_tree(tem.get_root(), '', char_freq)


    output = open(outputfilename, 'wb')
    code = ''
    currnode = tem.get_root()
    for x in range(leaf_node_size*5+4, filesize):
        c = six.byte2int(filedata[x])
        for i in range(8):
            if c&128:
                code = code + '1'
            else:
                code = code + '0'
            c = c<<1
        while len(code) > 24:
            if currnode.isleaf():
                tem_byte = six.int2byte(currnode.get_value())
                output.write(tem_byte)
                currnode = tem.get_root()
       
            if code[0] =='1':
                currnode = currnode.get_right()
            else:
                currnode = currnode.get_left()
            code = code[1:]
    #final 24
    sub_code = code[-16:-8]
    last_length = 0
    for i in range(8):
        last_length = last_length << 1
        if sub_code[i] == '1':
            last_length = last_length | 1

    code = code[:-16] + code[-8:-8 + last_length]
    while len(code) > 0:
        if currnode.isleaf():
            tem_byte = six.int2byte(currnode.get_value())  
            output.write(tem_byte)
            currnode = tem.get_root()
        if code[0] == '1':
            currnode = currnode.get_right()
        else:
            currnode = currnode.get_left()
        code = code[1:]

    if currnode.isleaf():
        tem_byte = six.int2byte(currnode.get_value())
        output.write(tem_byte)
        currnode = tem.get_root()
    output.close()


if __name__ == '__main__':
    #获取用户输入
    if len(sys.argv) != 4:
        print "Please input flag(0|1) inputfilename outputfilename"
        exit(0)
    else:
        FLAG = sys.argv[1]
        INPUTFILE = sys.argv[2]
        OUTPUTFILE = sys.argv[3]
    
    if FLAG == '0':
        print 'compress file'
        compress(INPUTFILE,OUTPUTFILE)
    else:
        print 'decompress file'
        decompress(INPUTFILE,OUTPUTFILE)
