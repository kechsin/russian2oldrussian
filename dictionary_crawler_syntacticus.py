import requests
import json

words = []
for i in range(0, 13300, 100):
    words_i = requests.get(f'https://tekstlab.uio.no/syntacticus-api/dictionaries/syntacticus:20180920:orv/lemmas?limit=100&offset={i}').json()
    words += words_i["data"]

to_write = ""
for i in words:
    line = f"{i['lemma']},{i['part_of_speech']},{i['glosses'].get('rus', '').replace(',', ';')}\n"
    to_write += line

with open("syntacticus_dictionary.csv", "w", encoding="utf8") as f:
    f.write(to_write)
