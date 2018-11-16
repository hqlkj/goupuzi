import urllib.request
import requests
import re
url = "http://www.goupuzi.com/"
response = urllib.request.urlopen(url)
html = response.read().decode("gbk")
print(type(html))
infos1 = re.findall(r'<div class="clearfix">.*?<img src="(.*?)".*?<a class="exhibit_list_title".*?>(.*?)</a>.*?</div>',html,re.S)
#infos2 = re.findall(r'<div class="clearfix">.*?<img src="(.*?)".*?<a class="exhibit_list_title".*?>(.*?)</a>.*?<span class="exhibit_zxrom">(.*?)</span>.*?<div class="thread_newsk_info">.*?<span>(.*?)</span>.*?<span class="thread_newsk_type">(.*?)</span>.*?</div>',html,re.S)
# infos = infos1+infos2
path = r"D:\狗铺子\images"
file = open("狗铺子.txt","a+",encoding="utf-8")
n = 1
for info in infos1:
    print(info)
    file.write(str(info)+"\n")
    imgurl = info[0]
    print(imgurl)
    res = requests.get(imgurl)
    img = open(path+"\\"+str(n)+".jpg","wb")
    img.write(res.content)
    img.close()
    n += 1
file.close()




