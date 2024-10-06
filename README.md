# russian2oldrussian
### Описание программ в папке, посвящённой сбору параллельных текстов:
crawler бегает по http://lib.pushkinskijdom.ru/Default.aspx?tabid=2070 и находит ссылки на все тексты и кладёт их в texts_urls.  text_taker проходит по этому списку и собирает файлы в папку texts. errors собирает если что-то в краулере хотело выдать ошибку, wrong_len собирает если что-то в text_taker'e получилось с разным количеством переводов и оригиналов.
### Apertium-файлы
Здесь находятся не все файлы, необходимые для Apertium, а только те, которые я меняла или использовала для ориентира.
Все файлы есть в https://github.com/kechsin/apertium-rus-orv.
apertium-rus-olr.rus.dix и apertium-rus-olr.olr.dix - морфологические словари. Второй из них я составляла, а первый использовала как образец для второго.
apertium-rus-olr.rus-olr.dix - двуязычный словарь.
apertium-rus-olr.rus-olr.t1x - правила трансфера.
### Файлы, посвящённые получению словарей
Сначала dictionary_crawler_syntacticus.py скачивает слова с сайта https://syntacticus.org/dictionary/syntacticus:20180920:orv и добавляет их в файл syntacticus_dictionary.csv. 
Файл what_declension.py определяет склонение существительного. Если удалось, то слово попадает в nouns_with_declension.txt, если нет, то в for_manual.txt. manual_declension - программа для введения склонений сущ. из for_manual.
put_nouns_to_dix кладёт все слова из nouns_with_declension в apertium-rus-olr.olr.dix
Для глаголов подобное, но вместо what_declension.py будет what_verb_type.py, кладётся в verbs_with_declension. Ничего ручного нет. В морфологический словарь кладётся тоже с помощью put_nouns_to_dix.
Берёт оно глаголы или существительные, зависит от того, закомментирована первая строчка или вторая. 
Файл bilingual.py берёт слова из syntacticus_dictionary.csv, у которых есть перевод, и помещает их в apertium-rus-olr.rus-olr.dix
### Другие файлы
Про поднимание апертиума.docx - описание процесса запуска апертиума.
