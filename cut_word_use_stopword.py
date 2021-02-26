import jieba
#import wordcloud
import pandas as pd
import matplotlib as plt

f = open("comments.txt", 'r',encoding = 'UTF-8')
text = f.read()
f.close()

cut_text = jieba.lcut(text)#将原文件分为词语
f = open("停用词.txt",encoding = 'UTF-8')#读取停用词
stop_words = "".join(f.read())
stop_words.join('\n\t')
f.close()

stop_words_list = stop_words.split('\n')
stop_words_list.append('\n')
filted_text_list = []
for s in cut_text:    
    if s not in stop_words_list:        
        filted_text_list.append(s)
words_dic = {}
for s in filted_text_list:
    words_dic[s] = words_dic.get(s, 0) + 1#统计词频
words_list = list(words_dic.items())
words_list.sort(key=lambda x: x[1],reverse=True)
words_dic = dict(words_list)
cloud_words_list = list(words_dic.keys())
cloud_words = " ".join(cloud_words_list[:30])#取排名前三十的词语
print(cloud_words)
with open('关键词.txt','a',encoding = 'UTF-8') as f:
    for data in cloud_words:
        f.write(data)