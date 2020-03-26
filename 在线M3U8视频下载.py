import json
import re
import urllib
import urllib.request
#https://videos3.jsyunbf.com/2018/06/18/PU5UPM6xORQS1Edo/
def download(url,path):
    urllib.request.urlretrieve(url,path)

text1=open('text.m3u8',mode='r')
text=text1.read()
furl='https://videos3.jsyunbf.com/2018/06/18/PU5UPM6xORQS1Edo/'
p=re.compile('#EXTINF:.*?out(.*?).ts',re.S)
lll=re.findall(p,text)
path="d:\\moviedown\\"
for i in lll:
    allurl=furl+"out"+str(i)+".ts"
    print(allurl)
    download(allurl,path+"out"+str(i)+".ts")