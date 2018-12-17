#-*-coding:utf-8-*-
 
import requests
import re
key="qq.com"
sites=[]
sites1=[]
match='style="text-decoration:none;">(.*?)/'
match1='<cite>(.*?)<'
for i in range(48):
    i=i*10
    url="http://www.baidu.com.cn/s?wd=site:"+key+"&cl=3&pn=%s"%i
    bing="https://cn.bing.com/search?q=domain:"+key+"&sk=&&first=%s"%i
    response=requests.get(url).content
    response1=requests.get(bing).content
    subdomains=re.findall(match,response)
    subdomains1=re.findall(match1,response1)
    sites += list(subdomains)
    sites1 +=list(subdomains1)
site=list(set(sites)) #set() quzhong
site1=list(set(sites1))
sites=list(set(site+site1))
#print sites
print "The number of site is %d"%len(sites)
for i in sites:
    print i
