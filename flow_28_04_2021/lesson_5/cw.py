"""SQL и базы данных

Создать базу данных с названием order_service_db. Создать в ней несколько таблиц:

Таблица ЗАЯВКИ (orders)
- id заявки (order_id) - целое число
- дата создания (created_dt) - текст
- дата обновления заявки (updated_dt) - текст
- тип заявки (order_type) - текст
- описание (description) - текст
- статус заявки (status) - текст
- серийный номер аппарата (serial_no) - целое число
- id создателя заявки (creator_id) - целое число

Таблица СОТРУДНИКИ (employees)
- id сотрудника (employee_id) - целое число
- ФИО (fio) - текст
- должность (position) - должность
- id подразделения (department_id) - целое число

Таблица ПОДРАЗДЕЛЕНИЯ (departments)
- id подразделения (department_id) - целое число
- id руководителя (director_id) - целое число
- название подразделения (department_name) - текст

Написать код создания таблиц на языке SQL, предусмотреть необходимые ограничения.
"""

# ЧТО ТАКОЕ БАЗА ДАННЫХ?
# Простым языком, база данных это структурированное хранилище информации. В зависимости от структуры
# построения баз данных они могут быть (неполный список):
# - реляционные (Postgresql, SQLite)
# - документоориентированные (MongoDB)
# - time-series (InfluxDB)

# В реляционных базах данных вся информация хранится в виде таблиц, которые могут быть связанны между собой.


# SQL - SQL — простыми словами, это язык программирования структурированных запросов
# (SQL, Structured Query Language), который используется в качестве способа общения с базами данных.

# SQLite - самая легковесная БД, её структура умещается в файл, который можно перекидывать хоть
# по сети или в телеграмме или по почте.

# БАЗОВЫЕ КОМАНДЫ:
# СОЗДАНИЕ БАЗЫ ДАННЫХ SQLite3 - создаём через SQLite Studio, через кнопку new database, где указываем путь к файлу

# СОЗДАНИЕ ПРОСТОЙ ТАБЛИЦЫ:
"""CREATE TABLE products (
    product_id INTEGER,
    description TEXT,
    quantity INTEGER
    );
"""

# ХОЗЯЙКЕ НА ЗАМЕТКУ: id - плохое имя для колонки, лучше выбирать другое имя, например product_id

# Если попытаться повторно создать ту же самую таблицу, то вылезет ошибка. Бывают ситуации, например когда
# нужно повторно прогнать миграции в базе.(это набор команд, которые выстраивают структуру базы) и тогда
# полезно добавлять проверку на существование таблицы:

# СОЗДАНИЕ ПРОСТОЙ ТАБЛИЦЫ С ПРОВЕРКОЙ НА СУЩЕСТВОВАНИЕ:
"""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER,
    description TEXT,
    quantity INTEGER
    );
"""

# У нас по бизнес-требованиям получается, что каждый продукт в базе должен быть уникальным по своему id,
# поэтому можно и нужно ввести ограничение по полю product_id.

"""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY, -- теперь у нас product_id будет уникальным идентификатором
    description TEXT,
    quantity INTEGER
    );
"""

# ТАБЛИЦУ МОЖНО ОЧЕНЬ ПРОСТО УДАЛИТЬ (трудно найти, легко потерять и невозможно забыть):
"""
DROP TABLE IF EXISTS products
"""

# ВЫБОРКА ДАННЫХ ИЗ ТАБЛИЦЫ:
"""
SELECT * FROM products; -- все колонки, вся таблица
"""

# ВСТАВКА ДАННЫХ В ТАБЛИЦУ:
"""
INSERT INTO products VALUES (123, 'Лук', 120); -- вставка по всем колонкам

INSERT INTO products (product_id) VALUES (1); -- вставка в конкретное поле
"""
# Мы можем управлять обязательность полей в базе при создании таблицы:
"""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY,
    description TEXT NOT NULL, -- теперь при вставке данных эта колонка не может оставаться NULL
    quantity INTEGER NOT NULL -- теперь при вставке данных эта колонка не может оставаться NULL
    );
"""

# Теперь при попытке записать данные, в которых мы что-то недодали будет падать ошибка
# А теперь давайте представим, что мы хотим, чтобы у нас id присваивался базой автоматически и
# возвращался нам в качестве ответа:

"""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL, -- теперь при вставке данных эта колонка не может оставаться NULL
    quantity INTEGER NOT NULL -- теперь при вставке данных эта колонка не может оставаться NULL
    );
"""

# # Теперь id явно вставлять не нужно:
# """
# INSERT INTO products (description, quantity) VALUES ('Лук', 120) RETURNING product_id;
# """

# Теперь про отношения - можно связыавть таблицы через FOREIGN KEY - по сути наши таблицы связываются друг с другом
# через какую-либо колонку.

"""
CREATE TABLE IF NOT EXISTS shops (
    shop_id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    address TEXT NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products (product_id) -- указываем какие колонки будут связанными
    );
"""

# Теперь у нас не получится вставить в таблицу, которая учитывает наличие продуктов в магазинах те продукты, которые
# отсутствут в базе products


"""
CREATE TABLE IF NOT EXISTS shops (
    shop_id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    address TEXT NOT NULL,
    product_id INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products (product_id)
    ON UPDATE SET NULL  -- при изменении данных в соответствующей колонке в родительской таблице значение станет NULL
    ON DELETE CASCADE -- при удалении данных из родительской таблице данные в дочерней тоже будут удалены
    );
"""

# Случаются ситуации, когда нужно изменить структуру существующей таблицы. Для этого используется механизм ALTER TABLE
"""
ALTER TABLE shops ADD COLUMN created_dt TEXT;
"""

# Индексы - механизм, позволяющий оптимизировать поиск по таблице. Напоминает ситуацию с теефонной книгой.

# Для того, чтобы удобно подключаться к базе и просматривать данные можно использовать DBeaver