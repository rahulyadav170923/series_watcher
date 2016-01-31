import urllib2
from bs4 import BeautifulSoup
from selenium import webdriver
domain_url="http://thewatchseries.to"
base_url="http://thewatchseries.to/serie/"

def get_series(show):
    url=base_url+show
    r=urllib2.urlopen(url).read()
    soup=BeautifulSoup(r)
    series=soup.find_all("div",itemprop="season")
    dict=[]
    for i in range(0,len(series)):
        episodes=series[i].find_all("a",title="Unwatched episode")
        episode_list=[]
        for j in range(0,len(episodes)):
            episode_list.append({"text":episodes[j].span.text,"link":"http://thewatchseries.to"+episodes[j].attrs["href"]})
        dict.append({"text":series[i].a.text,"link":series[i].a.attrs["href"],"episode_list":episode_list})
    return dict

def download(url):
    complete_url=url
    driver = webdriver.PhantomJS(executable_path="/home/rahul/Desktop/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")
    driver.implicitly_wait(10)
    driver.get(complete_url)
    html=driver.page_source
    soup=BeautifulSoup(html)
    p=soup.find("a",title="gorillavid.in")
    complete_url=domain_url+p.attrs["href"]
    driver.get(complete_url)
    html=driver.page_source
    soup=BeautifulSoup(html)
    x=soup.find("a",class_="push_button blue")
    complete_url=x.attrs["href"]
    return complete_url
