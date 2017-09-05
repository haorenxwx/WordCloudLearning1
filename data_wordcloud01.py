import wordcloud as wc
import matplotlib.pylab as plb
import pandas as pda
#import pymysql

#conn=pymysql.connect(host="127.0.0.1",user="root",password="karen12345",db="******")
#sql1="select name from *****"

#cur=conn.cursor()
#cur.execute(sql1)
#h=pda.read_table("E:/电子书/《那些回不去的少年时光》.txt")
h=pda.read_csv("E:/电子书/《那些回不去的少年时光》.txt",sep='\t',encoding='utf-8')


print(h)

'''
name=" "
for i in cur:
	name=name+str(i[0])+" "
font=r"C:\WINDOWS\Fonts\simhei.tff"
mywc=wc.WordCloud(collocations=False,font_path=font).generate(name)
plb.imshow(mywc)
plb.show()
'''

#for i in h:
#	txt=txt+str(i[0])

