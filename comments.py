import re
import json
import requests
def getinfo():
    global cursor,source
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
    for i in range(0,1271):
        url = 'https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=' + cursor + '&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=' + source
        data = requests.get(url, headers=headers).content.decode()
        
        cursor = re.findall('"last":"(.*?)"',data,re.S)[0] #下一页URL的cursor
        source = str(int(source)+1) #下一页URL的source
        
        comment = re.findall('"content":"(.*?),"',data,re.S) #爬取当前页的评论
        comments.append(comment)
    return comments

def writejson(comments):
    with open('comments.json','a',encoding = 'UTF-8') as jsonfile:
        for info in comments:
            for data in info:
                jsonfile.write(data)
                jsonfile.write('\n')

comments=[]
cursor='0'
source = '1614062141061'
comments = getinfo()
writejson(comments)