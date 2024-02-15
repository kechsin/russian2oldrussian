from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

f = open("texts_urls.txt")
links = f.readlines()
f.close()

base_url = "http://lib.pushkinskijdom.ru"
for k in range(len(links)):
    links[k] = links[k].strip()
    if links[k][0:4] != "http":
        links[k] = base_url + links[k]

print(links[0])

texts = []
translates = []

for i in links:
    texts_i = []
    translates_i = []
    response = requests.get(i)
    soup = BeautifulSoup(response.text, "html.parser")
    for par_txt in soup.findAll('div', {'id': "parallel"}):
        paragraphs = par_txt.findChildren()
        text_piece = ""
        transl_piece = ""
        for elem in paragraphs:
            if elem.has_attr('class') and elem['class'][0] == 'original':
                text_piece += elem.text
                if transl_piece:
                    translates_i.append(transl_piece)
                    transl_piece = ""
            if elem.has_attr('class') and elem['class'][0] == 'translation':
                transl_piece += elem.text
                if text_piece:
                    texts_i.append(text_piece)
                    text_piece = ""
            if elem.has_attr('class') and elem['class'][0] == 'clear':
                if transl_piece:
                    translates_i.append(transl_piece)
                    transl_piece = ""
        if text_piece:
            texts_i.append(text_piece)
        if transl_piece:
            translates_i.append(transl_piece)
        texts.append(texts_i)
        translates.append(translates_i)
        if len(translates_i) != len(texts_i):
            f = open("wrong_len.txt", "a")
            f.write(i)
            f.close()

for txt_num in range(len(texts)):
    txt_table = []
    for i in range(len(texts[txt_num])):
        table_line = texts[txt_num][i] + "\t" + translates[txt_num][i] + "\n"
        txt_table.append(table_line)
    f = open(f"texts/{txt_num}.csv", "w", encoding="utf-8")
    for i in txt_table:
        f.write(i)
    f.close()
