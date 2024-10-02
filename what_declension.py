with open("about_dictionaries/syntacticus_dictionary.csv", encoding="utf8") as f:
    words = f.readlines()

nouns = []
for i in words:
    if i.split(",")[1][0] == "N":
        nouns.append(i.split(",")[0].strip().lower())

words2 = []
manual = []
for i in nouns:
    print(i)
    if i[-1] == "а":
        words2.append([i, "сущ", "n_а-склон_f"])
        continue
    if i[-1] == "я":
        words2.append([i, "сущ", "n_jа-склон_f"])
        continue
    if i[-1] == "ъ":
        if i in ["cынъ", "врьхъ", "полъ", "волъ", "медъ", "ледъ"]:
            words2.append([i, "сущ", "n_u-склон_n"])
            continue
        words2.append([i, "сущ", "n_o-склон_m"])
        continue
    if i[-1] == "о":
        # words2.append([i, "сущ", "n_o-склон_n"])
        manual.append([i, "о-склон, или c ес"])
        continue
    if i[-1] == "ь":
        # words2.append([i, "сущ", "n_jo-склон_m"])
        manual.append([i, "о-склон, или i-склонение (тогда какого рода)"])
        continue
    if i[-1] == "e":
        words2.append([i, "сущ", "n_jo-склон_n"])
        continue
    if i[-1] == "ѥ":
        words2.append([i, "сущ", "n_jo-склон_n_(ѥ)"])
        continue
    if i[-1] == "ы":
        # words2.append([i, "сущ", "n_C-склон_m_(ен)"])
        manual.append([i, "ен или ъв"])
        continue
    if i[-1] == "ѧ":
        manual.append([i, "ен или ят"])
        continue
    if i[-1] == "и":
        words2.append([i, "сущ", "n_C-склон_f_(ер)"])
        continue

with open("for_manual.txt", "w", encoding="utf8") as f:
    f.writelines([str(i) + "\n" for i in manual])

with open("nouns_with_declensions.txt", "w", encoding="utf8") as f:
    f.writelines([",".join(i) + "\n" for i in words2])

