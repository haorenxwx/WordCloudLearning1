#-*- coding: utf-8 -*-

#test change in github
#from wordcloud import wordcloud
import wordcloud as wc
import codecs
import jieba
#import jieba.analyse as analyse
from scipy.misc import imread
import os
from os import path
#import matplotlib.pyplot as plt
import matplotlib.pylab as plt
#from PIL import Image, ImageDraw, ImageFont
import pandas as pda
from PIL import Image
from numpy import array


#path="E:/电子书/《那些回不去的少年时光》.txt"
path="E:/电子书/BL Novel/柴鸡蛋/《你丫上瘾了？》BY：柴鸡蛋.txt"
data=open(path,"r",encoding="gbk").read()
#data=open(path,"r",encoding="UTF-8").read()


#h=pda.read_table("E:/电子书/《那些回不去的少年时光》.txt")
#comment_text = open('E:/电子书/《那些回不去的少年时光》.txt',encoding='UTF-8','r').read()
#print(comment_text)

#cut_text = " ".join(jieba.cut(h))
#d=path.dirname(_file_)#当前文件所在文件夹目录

cutdata=jieba.cut(data)
alldata=""
for i in cutdata:
	alldata=alldata+" "+str(i)#通过迭代器把词语连起来并用空格隔开

color_mask = imread ("E:/study/python/onepiece.png")#读取背景图片
#font=r"E:/study/python/HYQiHei-25J.ttf"
font=r"E:/study/python/simhei.ttf"
cloud=wc.WordCloud(
	collocations=False,
	#font_path ="HYQiHei-25J.ttf",
	font_path=font,
	#指定字体
	#font_path =path.join(d,"HYQiHei-25J.ttf"),
	background_color='white',
	#设置背景色
	mask=color_mask,
	#词云形状
	max_words=500,
	max_font_size=40
)
word_cloud =cloud.generate(alldata)
#word_cloud =cloud.generate(h)
#word_cloud =cloud.generate(cut_text)
word_cloud.to_file("losttime.jpg")

plt.imshow(word_cloud)
plt.axis('off')
plt.show()
