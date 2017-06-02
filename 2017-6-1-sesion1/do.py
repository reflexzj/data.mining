# coding:utf-8
__author__ = 'zhangjian'
__date__ = '2017-06-01'

from sentence import Sentence
import os

#遍历指定目录，显示目录下的所有文件名
def eachFile(filepach):
    files = []
    pathDir = os.listdir(filepach)
    for allDir in pathDir:
        # child = os.path.join("%s%s" %(filepach, allDir))
        # print child.decode('gbk')
        files.append(filepach+allDir)
    print files
    return files

def handle(filename):
    url_text = filename

    sentence = Sentence()

    f = open(url_text, 'r')
    txt_string = f.read().strip().decode('utf-8').replace('\n', ' ')

    # 获取中文内容
    step_1 = sentence.filter_chinese_character(txt_string)
    # 移除停用词
    step_2 = sentence.remove_stop_word(step_1)
    # 移除重复词
    # step_3 = sentence.remove_repeat_word(step_2)

    return step_2

if __name__ == '__main__':

    # 获取九个文件夹的目录
    datas = []
    #将rar文件解压到当前目录
    filepach = 'data/data/'
    datas = eachFile(filepach)

    #获取每个文件夹下的文件目录
    fopen = open('data/result.txt', 'w')
    for each in datas:
        filepach = each+'/'
        files = eachFile(filepach)

        #遍历所有的每个文件夹下的所有txt文件
        for filename in files:
            data = handle(filename)
            print data
            if data:
                fopen.write(data+'\n')
            print filename + 'has done'
