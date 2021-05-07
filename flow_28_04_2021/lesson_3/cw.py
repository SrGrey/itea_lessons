"""
Домашнее задание:
1. Создать свой собственный репозиторий. При создании указать наличие файла Readme и gitignore для Python.
    - создать ветку develop и переключиться на работу в ней
    - создать папки для прошудших 1, 2 и 3 уроков
    - в папках создать файлы homework и добавить туда домашние задания согласно урокам
    - сделать коммит и пуш
    - поставить pull-request в github
    - поделиться с товарищами PR, посмотреть чужие PR, оставить комментарии при необходимости
    - сделать merge, обновить главную ветку с помощью команды pull на локальной тачке.

2. Покрыть тестами задачу из прошлой домашки с матрицами: сложение, умножение на число, возникновение ошибки.
"""
#############################################################
############################ GIT ############################
#############################################################

# Что такое «система контроля версий» и почему это важно? Система контроля версий -
# это система, записывающая изменения в файл или набор файлов в течение времени и позволяющая вернуться позже
# к определённой версии.

# GIT - распределённая система управления версиями

# Чтобы присоединиться к работе над каким-либо проектом нужно сначала клонировать себе репозиторий этого проекта:
# git clone <адрес репозитория>

# По умолчанию в репозитории есть 1 единственная ветка: она называется master или main. Эта ветка хранит эталон
# вашего проекта, который вы катите в прод (отдаёте конечному пользователю)

# От основной ветки в процессе работы над проектом будут отпочковываться новые ветки. Зачем нужно делать новые ветки?
# Для того, чтобы можно было работать над проектом качественно и независимо от задач других коллег, а также для
# того, чтобы можно было контролировать все изменения по нему.

# ОСНОВНЫЕ СУЩНОСТИ:
# репозиторий - это по сути проект, над которым вы работаете и над которым надзирает GIT
# удалённый репозиторий - это проект в том виде, в котором он хранится на сервере
# локальный репозиторий - это проект в том виде, в котором он хранится на локальной машине
# ветка - это "альтернативная вселенная" вашего проекта, где вы вносите изменения согласно задаче
# коммит - это фиксация изменений в ветке

# ОСНОВНЫЕ КОМАНДЫ И ИХ СМЫСЛ:
# clone - клонировать репозиторий из удалённого репозитория
# commit - зафиксировать изменения в ветке
# push - отправить изменения в удалённый репозиторий
# checkout - переключиться на определённый коммит или ветку

# Типичный flow разработчика в команде здорового человека:
# - получил задачу, создал новую ветку от актуального master/main
# - внес необходимые изменения, которые предусматриваются задачей
# - протестировал свой код, убедился в правильности решения задачи
# - сделал commit изменений (фиксирование) и push (отправка в удалённый репозиторий)
# - поставил pull-request (запрос на вливание ветки в main/master) и сбросил ссылку на него коллегам для ревью
# - после того, как коллеги отсмотрели PR (pull-request) они либо оставляют комментарии на доработку, либо ставят +
# - если есть комментарии, то мы дорабатываем код в той же ветке и просто ещё раз коммитимся и пушимся
# - если всё хорошо и наш PR одобрен, то мы нажимаем merge и изменения вливаются в основную ветку
# - берем новую задачу в работу, переключаемся на main/master ветку, актуализируем её с помощью pull

# ХОЗЯЙКЕ НА ЗАМЕТКУ: pull-request ставится НА ВЕТКУ, а не на какой-то определённый коммит! То есть если вы поставили
# pull-request и потом в свою ветку.

# ХОЗЯЙКЕ НА ЗАМЕТКУ: перед тем, как приступить к работе над задачей и отпочковываться от ветки main/master,
# обязательно стоит сделать git pull - это заберет актуальные изменения из удалённого репозитория.

# ХОЗЯЙКЕ НА ЗАМЕТКУ: если вы чувствуете, что нагородили что-то очень непонятное, то иногда бывает лучше создать
# новую ветку и перенести туда свои изменения руками и попробовать снова поставить PR.

# Рекомендую посмотреть:
# https://www.youtube.com/watch?v=KMToEZLP97Y&t=2s
# https://www.youtube.com/watch?v=Ag_5mV5Qh1Y&t=612s

#############################################################
########################### Pytest ##########################
#############################################################

# отличная книга по пайтесту - https://habr.com/ru/post/448782/
# зачем вообще тестировать свой код?
# 1. Уверенность, что задача выполнена правильно и мы катим в прод качественное решение
# 2. Уверенность в том, что наши изменения в рамках задачи не поломают прежнюю функциональность

# TDD - test drive development - разработка через тестирование. подход заключается в том, что мы сначала пишем
# тесты, а потом пишем сам код.

# pip install pytest - для установки библиотеки pytest
# условия для запуска тестов:
# 1. у нас должна быть папка с названием tests
# 2. имена всех тестовых файлов в папке/папках должны начинаться с test_
# 3. имена всех тестовых функций в файлах должны начинаться с test_

# напишем и протестируем простую функцию:

def divisor(a, b):
    return a / b

# Тестовый кейс 1: 1 и 2 -> ожидаем 0.5
# Тестовый кейс 2: 100 и 50 -> ожидаем 2
# Тестовый кейс 3: 1 и 0 -> ожидаем возникновение ошибки ZeroDivisionError
# реализация тестовых кейсов находится в модуле tests/test_divisor.py

##########################################################################
############################ Работа с файлами ############################
##########################################################################

# работа с файлами в Python это на самом деле работа с обвязкой вокруг файла!
from io import TextIOWrapper

f_o = open("testfile.txt", "w")  # на самом деле тут создаётся объект TextIOWrapper
f_o.write("test_string\n")
f_o.write("test_string\n")
f_o.write("test_string\n")
f_o.write("test_string\n")
f_o.close()

# режимы для взаимодействия с файлами: w, r, a + ещё несколько, в зависимости от типа файла и целей
f_o = open("testfile.txt", "r")
for line in f_o:
    print(line, end="")
f_o.close()

# бывает так, что у нас открыто очень много файлов (по ошибке, потому что не предусмотрен механизм закрытия)
# f_o_lst = [open("testfile.txt", "r") for _ in range(100_000)] # OSError: Too many open files: 'testfile.txt'
# чтобы такого не было надо отлавливать потенциальные ошибки:

try:
    f_o = open("testfile.txt", "r")
except Exception as err:
    print(err)
finally:
    f_o.close()

# такой вариант не самый лучший для того, чтобы поддерживать удобство кода. Специально для таких случаев придумали
# менеджеры контекста

##########################################################################
########################### Менеджер контекста ###########################
##########################################################################
f_o = open("testfile.txt", "r")
with f_o:
    print("Это выполнение какого-то контекста")

# объект после with должен обладать методами __enter__ и __exit__. Давайте напишем кастомный класс и посмотрим,
# как это работает


class MyClassForContextMan:
    def __enter__(self):
        print(f"Вызывается метод __enter__ у экземпляра {self}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Вызывается метод __exit__ у экземпляра {self}")
        if exc_val:
            print(f"И кстати тут произошла вот такая ошибка с вот такой информацией о ней: "
                  f"{exc_type}, {exc_val}, {exc_tb}")


ex_for_context = MyClassForContextMan()

# штатная работа:
with ex_for_context:
    print(f"Выполнение контекста для {ex_for_context}")


# а теперь посмотрим на работу при возникновении ошибки:
with ex_for_context:
    print(f"Выполнение контекста для {ex_for_context}")
    raise ValueError("Очень страшная ошибка!")

# менеджеры контекстов - ваш бро! Используйте их когда поключаетесь к БД, читаете или пишете в файлы и прочих прелестях,
# где работа с ними предусмотрена.
