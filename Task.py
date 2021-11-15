#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    school = {'1а': 18, '1б': 15, '2а': 25, '2б': 31, '3a': 22, '3б': 19, '4а': 24, "4б": 27}
    while True:
        n = input('Введите название операции >>> ')
        if n == 'change':
            school.update({input(f'Название изменяемого класса: '):
                        int(input(f'Количество учеников изменяемого класса: '))})
        elif n == 'new':
            school.update({input(f'Название класса №: '): int(input(f'Количество учеников класса №: '))})
        elif n == 'remove':
            del school[input(f'Название расформировываемого класса: ')]
        elif n == 'print':
            print(school)
        elif n == 'sum':
            print(sum(school.values()))
        elif n == "help":
          print('change - Изменилось количество учеников:')
          print('new - В школе появился новый класс')
          print('remove - В школе был расформирован (удален) класс')
          print('print - Выгрузка данных')
          print('sum - Число учеников')
          print('exit - Выход')
        elif n == 'exit':
            break
            