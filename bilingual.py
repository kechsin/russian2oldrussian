with open("syntacticus_dictionary.csv", encoding="utf8") as f:
    words = f.readlines()

transl_words = []
for i in words:
    parts = i.split(',')
    if parts[-1] != '\n':
        transl_words.append([parts[0], parts[-1].split(';')[0].strip()])

with open("apertium-rus-olr.rus-olr.dix", "a", encoding="utf8") as f:
    for i in transl_words:
        f.write(f'     <e><p><l>{i[1]}<s n="n"/></l><r>{i[0]}<s n="n"/></r></p></e>\n')
    f.write("    </section>\n")
    f.write("</dictionary>")