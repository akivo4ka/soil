**Схема БД:**
![ESOIL](https://user-images.githubusercontent.com/8759199/124818183-9f758400-df62-11eb-8726-2ca02c558d87.png)

Исходный файл схемы: 
* скачать https://github.com/akivo4ka/soil/blob/main/esoil.drawio
* открыть с помощью https://app.diagrams.net/

**[tables_descript.xlsx](https://github.com/akivo4ka/soil/blob/main/tables_descript.xlsx)**:
Первая страница (tables) содержит названия всех таблиц.
Остальные страницы составлены по следующему принципу:
- название страницы соответсвует названию таблицы в БД
- на странице перечислены названия и тип колонок таблицы; также указыввается, является ли данная колонка ForeignKey, например `integer references SOIL_DATA(ID)`

Пример: страница **SOIL_DATA_PHYS**
- относится к таблице `SOIL_DATA_PHYS`
- содержит описание структуры этой таблицы

![image](https://user-images.githubusercontent.com/8759199/124814421-e1e89200-df5d-11eb-9fb0-9eb35af193cb.png)

Отмечу, что на странице SOIL_DATA некоторые колонки выделены цветом - в зависимости от типа свойства (химическое, физическое).

Описание данных
(если в excel-файле несколько страниц, то актуальной является страница с название data)

**Семантическая часть**
1. [SOIL_SEM](https://github.com/akivo4ka/soil/blob/main/soil_sem.xlsx) - Список почв ЕГРП - 205 типов почв (http://egrpr.esoil.ru/content/1sem.html) 
2. [SOIL_MAIN_HORIZONS](https://github.com/akivo4ka/soil/blob/main/soil_main_horizons.xlsx) - Почвенные горизонты: органические, органо-минеральные, минеральные (http://egrpr.esoil.ru/content/1dia.html)
3. [SOIL_ADD_HORIZONS](https://github.com/akivo4ka/soil/blob/main/soil_add_horizons.xlsx) - Дополнительные свойства почвенных горизонтов (http://egrpr.esoil.ru/content/1dia.html)
4. SOIL_PROFILE - Почвенный профиль - предусмотреть таблицу на будущее (http://egrpr.esoil.ru/content/1dia.html) - В настоящий момент таблица не заполнена. Данные для заполнения можно взять из столбца PFRML таблицы SOIL_DATA
5. [SOIL_MORPH](https://github.com/akivo4ka/soil/blob/main/soil_morph.xlsx) - Морфологические свойства почв (http://egrpr.esoil.ru/content/1svo.html)
6. [SOIL_MORPH_ELEM](https://github.com/akivo4ka/soil/blob/main/soil_morph_elem.xlsx) - Свойства морфологических элементов почв (http://egrpr.esoil.ru/content/1svo.html)
7. [SOIL_CHEM](https://github.com/akivo4ka/soil/blob/main/soil_chem.xlsx) - Химические свойства почв (http://egrpr.esoil.ru/content/1svo.html)
8. [SOIL_PHYS](https://github.com/akivo4ka/soil/blob/main/soil_phys.xlsx) - Физические свойства почв (http://egrpr.esoil.ru/content/1svo.html)

**[SOIL_DATA](https://github.com/akivo4ka/soil/blob/main/soil_data.xlsx)** - Описание свойств для каждого типа почвы (http://egrpr.esoil.ru/content/1DB.html)

Описание некоторых колонок данной таблицы:
* HISMMN - очень похоже на обозначение почевнных горизонтов, однако как их сопоставить, мне осталось непонятно (?)
* HISMSM - дополнительное свойство почвенных горизонтов (SOIL_ADD_HORIZONS)
* MOISTR-ADDMRF - морфологические свойства почв (SOIL_MORPH)
* LOSA-TEXTPHS - химические свойства почв (SOIL_CHEM)
* GRSCMP-ADPHYS - физические свойства почв (SOIL_PHYS)

(!) Важно заметить, что таблицы SOIL_MAIN_HORIZONS, SOIL_MORPH_ELEM не имеют связей с таблицей SOIL_DATA.

**Геометрическая часть**
* Таблица полигонов (http://egrpr.esoil.ru/content/1geo.html)
1. [SOIL_MAP](https://github.com/akivo4ka/soil/blob/main/soil_map.xlsx)
2. [SOIL_MAP_LEGEND](https://github.com/akivo4ka/soil/blob/main/soil_map_legend.xlsx)
3. [SOIL_MAP_PARENT_LEGEND](https://github.com/akivo4ka/soil/blob/main/soil_map_parent_legend.xlsx)
* Таблица композиции полигонов (http://egrpr.esoil.ru/content/1DB.html#composition)

**Python** скрипты для создания и заполнения таблиц данными из excel-файлов:
* Создание таблиц: [ipynb](https://github.com/akivo4ka/soil/blob/main/create_tables.ipynb) / [py](https://github.com/akivo4ka/soil/blob/main/create_tables.py)
* Заполнение таблиц: [ipynb](https://github.com/akivo4ka/soil/blob/main/insert_tables.ipynb) / [py](https://github.com/akivo4ka/soil/blob/main/insert_tables.py)

(!) На данный момент следующие таблицы не заполнены:
* SOIL_DATA_ADD_HORIZONS
* SOIL_DATA_MORPH
* SOIL_DATA_CHEM
* SOIL_DATA_PHYS
