# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
import os


class NotNameError(Exception):

    def __init__(self):
        self.message = 'Ошибка в указании имени'

    def __str__(self):
        return self.message


class NotEmailError(Exception):

    def __init__(self):
        self.message = 'Ошибка при вводе e-mail'

    def __str__(self):
        return self.message


def filling_check(file):
    with open(file, 'r', encoding='utf8') as ff, open('registrations_good.log', 'a+', encoding='utf8') as fg, open(
            'registrations_bad.log', 'a+', encoding='utf8') as fb:
        for line in ff:
            line = line[:-1]
            name, e_male, age = line.split(' ')
            age = int(age)
            if len(name) or len(e_male) or len(str(age)) != 0:
                if not name.isalpha():
                    fb.write(line + '\n')
                    raise NotNameError()

                elif '@' and '.' not in e_male:
                    fb.write(line + '\n')
                    raise NotEmailError()

                elif not 10 < age < 99:
                    raise ValueError('возраст не тот')
                else:
                    fg.write(line + '\n')



# TODO Каждый раз открывать файл на запись довольно ресурсозатратно.
#  Будет правильнее открыть все файлы до цикла.
#  Вы можете открыть сразу несколько файлов в одном контест менеджере.
#  with open('file1', 'w') as file1, open('file2', 'w') as file2:


name_file = 'registrations.txt'

try:
    filling_check(name_file)
except (NotNameError, NotEmailError, ValueError) as err:
    print(f'возникла ошибка {err}')
