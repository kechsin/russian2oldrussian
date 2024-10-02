# russian2oldrussian
### Описание программ в папке, посвящённой сбору параллельных текстов:
crawler бегает по http://lib.pushkinskijdom.ru/Default.aspx?tabid=2070 и находит ссылки на все тексты и кладёт их в texts_urls.  text_taker проходит по этому списку и собирает файлы в папку texts. errors собирает если что-то в краулере хотело выдать ошибку, wrong_len собирает если что-то в text_taker'e получилось с разным количеством переводов и оригиналов.
### Файлы, посвящённые получению словарей
Сначала dictionary_crawler_syntacticus.py скачивает слова с сайта https://syntacticus.org/dictionary/syntacticus:20180920:orv и добавляет их в файл syntacticus_dictionary.csv. 
Файл what_declension.py определяет склонение существительного. Если удалось, то слово попадает в nouns_with_declension.py, если нет, то в for_manual.txt. manual_declension - программа для введения склонений сущ. из for_manual.
put_nouns_to_dix кладёт все слова из nouns_with_declension в apertium-rus-olr.olr.dix
