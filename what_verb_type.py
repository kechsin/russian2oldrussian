with open("syntacticus_dictionary.csv", encoding="utf8") as f:
    words = f.readlines()

verbs = []
for i in words:
    if i.split(",")[1][0] == "V":
        verbs.append(i.split(",")[0].strip().lower())

words2 = []
for i in verbs:
    if i == "ѣсти":
        v_type = "v_ѣсти"
    elif i == "дати":
        v_type = "v_дати"
    elif i == "вѣдѣти":
        v_type = "v_вѣдѣти"
    elif i == "быти":
        v_type = "v_быти"
    elif i[-3:] == "ити":
        v_type = "v_и-ти_soft"
    elif i[-3:] == "ети":
        v_type = "v_е-ти_soft"
    elif i[-3:] == "ети":
        v_type = "v_е-ти_soft"
    elif i[-3:] == "яти":
        v_type = "v_я-ти_soft"
    elif i[-3:] == "ути":
        v_type = "v_у-ти_soft"
    elif i[-3:] == "ати":
        v_type = "v_а-ти_soft"
    words2.append([i, "гл", v_type])

with open("verbs_with_declensions.txt", "w", encoding="utf8") as f:
    f.writelines([",".join(i) + "\n" for i in words2])
