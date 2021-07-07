**Схема БД:**
![ESOIL](https://user-images.githubusercontent.com/8759199/124812788-fcba0700-df5b-11eb-8ce8-0fce35d36464.png)

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
