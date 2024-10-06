#with open("nouns_with_declensions.txt", encoding="utf8") as f:
with open("verbs_with_declensions.txt", encoding="utf8") as f:
    nouns = [(i.split(",")[0], i.split(",")[2].strip()) for i in f.readlines()]

to_write = []
for i in nouns:
    stem = i[0][:-1]  # так обычно выглядит основа
    line = f'    <e lm="{i[0]}"><p><l>{stem}</l><r>{i[0]}</r></p><par n="{i[1]}"/></e>\n'
    to_write.append(line)
to_write.append("</section>\n")
to_write.append("</dictionary>")

with open("apertium-rus-orv.orv.dix", "a", encoding="utf8") as f:
    f.writelines(to_write)