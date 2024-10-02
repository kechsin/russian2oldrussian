with open("for_manual.txt", encoding="utf8") as f:
    lines = f.readlines()

lines_write = []
to_repeat = []
counter = 0
for i in lines:
    if counter == 30:
        to_repeat.extend(lines[30:])
    i += 1
    print(i)
    decl_letter = input("Варианты: 'o', 'jo', 'i', 'ес', 'ен', 'ят'. ")
    decl_type = ""
    word = i.split("'")[1]
    if decl_letter == 'jo':
        gender = input("Род: f/m/n. ")
        if gender == 'm':
            decl_type = "n_*jo-склон_m"
        elif gender == 'n':
            decl_type = "n_*jo-склон_n"
        else:
            to_repeat.append(i)
    elif decl_letter == 'o':
        decl_type = "n_*o-склон_n"
    elif decl_letter == 'i':
        gender = input("Род: f/m/n. ")
        if gender == 'm':
            decl_type = "n_*i-склон_m"
        elif gender == 'f':
            decl_type = "n_*i-склон_f"
        else:
            to_repeat.append(i)
    elif decl_letter == 'ес':
        decl_type = "n_*C-склон_n_(ес)"
    elif decl_letter == 'ен':
        decl_type = "n_*C-склон_n_(ен)"
    elif decl_letter == 'ят':
        decl_type = "n_*C-склон_n_(ѧт)"
    else:
        to_repeat.append(i)
    lines_write.append(word + ",сущ," + decl_type + "\n")

with open('for_manual_2.txt', 'w') as f:
    f.writelines(to_repeat)
with open('nouns_with_declensions.txt', 'a') as f:
    f.writelines(lines_write)