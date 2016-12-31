# Поиск дубликатов

Программа предназначена для поиска дубликатов файлов. Под дубликатами поднимаются файлы, у которых одинаковые имена и размер.

# Как запустить

Для работы скрипта требуется интерпретатор Python 3.5.

Пример запуска программы в Linux:

```#!bash

$ python3 duplicates.py
Enter directory to find duples: 
/home/username/target # пользователь указывает полный путь к папке, в которой искать дубликаты
Analyzing files...

Found duplicates, size = 78514
/home/username/target/screenshot1.png
/home/username/target/stuff/misc/screenshot1.png

Found duplicates, size = 1540
/home/username/target/lol/notes.txt
/home/username/target/stuff/misc/notes.txt

```

Запуск на Windows происходит аналогичным образом.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
