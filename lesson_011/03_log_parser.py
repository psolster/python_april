# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

from collections import defaultdict


file_names = 'events.txt'
slice_date_start_1 = 0
slice_date_finish_1 = 17
slice_date_start_2 = 0
slice_date_finish_2 = 0
voc_time_nok = defaultdict(int)


def generate_line_w_nok(filename):
    with open(filename, 'r', encoding='cp1251') as ff:
        for line in ff:
            if line[29:-1] == 'NOK':
                time = line[slice_date_start_1:slice_date_finish_1] + ']'
                yield time


for data in generate_line_w_nok(filename=file_names):
    voc_time_nok[data] += 1
for key, it in voc_time_nok.items():
    print(key, it)
