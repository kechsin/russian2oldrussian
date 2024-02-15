from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

start_url = "http://lib.pushkinskijdom.ru/Default.aspx?tabid=2070"
base_url = "http://lib.pushkinskijdom.ru"

ua = UserAgent()
volumes_urls = []
response = requests.get(start_url)
soup = BeautifulSoup(response.text, "html.parser")
for i in soup.find_all('div', {'id': 'dnn_ctr5642_HtmlModule_lblContent'}):
    for link in i.find_all('a'):
        volume_link = link.get('href')
        if volume_link[0] == "/":
            volume_link = base_url + volume_link
        volumes_urls.append(base_url + str(link.get('href')))

texts_urls = []
text_set = set()
for i in volumes_urls:
    print(i)
    try:
        response = requests.get(i)
        soup = BeautifulSoup(response.text, "html.parser")
        for link in soup.find_all('div', {'class': "Normal"}):
            for smth in link.find_all('a'):
                link_href = smth.get('href')
                if type(link_href) == str:
                    if link_href not in text_set:
                        text_set.add(link_href)
                        texts_urls.append(link_href)
                else:
                    f = open("errors.txt", "a")
                    f.write("VOID " + link + "\n")
    except:
        f = open("errors.txt", "a")
        f.write("URLSLIST " + i + "\n")
        f.close()


f = open("texts_urls.txt", "w")
for i in texts_urls:
    f.write(i + '\n')
f.close()
