"""1. """

# бывает так, что у нас открыто очень много файлов (по ошибке, потому что не предусмотрен механизм закрытия)
# f_o_lst = [open("testfile.txt", "r") for _ in range(100_000)] # OSError: Too many open files: 'testfile.txt'
# чтобы такого не было надо отлавливать потенциальные ошибки:

try:
    f_o = open("testfile.txt", "w")
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
    # raise ValueError("Очень страшная ошибка!")

# менеджеры контекстов - ваш бро! Используйте их когда поключаетесь к БД, читаете или пишете в файлы и прочих прелестях,
# где работа с ними предусмотрена.


##########################################################################
################################ Docstrings ##############################
##########################################################################
class DockedClass:
    """Это просто класс который мы задокументировали"""

    def some_func(self):
        """Это функция, которую мы задокументировали"""
        pass


print(DockedClass.__doc__)
print(DockedClass.some_func.__doc__)

##########################################################################
############################ Абстрактные классы ##########################
##########################################################################

# Абстрактный класс - класс, который имеет хотя бы один абстрактный метод. Удивлены, не правда ли? Объясняем, что
# такое абстрактный класс через абстрактность) Попробую сказать проще:
# Абстрактный класс - это класс, который существует, как некий контракт или соглашение между разработчиками для
# удобства и порядка.
from abc import ABC, abstractmethod


class BaseClient(ABC):
    """Базовый клиент с методами, которые должны иметь ВСЕ клиенты-наследники"""

    @abstractmethod
    def ping(self):
        """Каждый клиент должен иметь возможность"""
        pass

    @abstractmethod
    def set_rps_for_client(self):
        """Устанавливаем rps для клиента"""
        pass
