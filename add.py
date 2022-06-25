from typing import List


def get_data():
    global a
    id = input('id: ')
    name = input('Имя: ')
    surname = input('Фамилия: ')
    clas = input('Класс')
    number = input('Номер телефона: ')
    a = [id,name,surname,clas,number]
    return a

def get_data1():
    global a
    id = input('id: ')
    name = input('Имя: ')
    patronymic = input('Отчество')
    surname = input('Фамилия: ')
    number = input('Номер телефона: ')
    a = [id,name,patronymic, surname,number]
    return a