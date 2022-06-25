import csv
from fileinput import close


def search():
    name = input('Введите Имя ученика: ')
    family = input('Введите Фамилию ученика: ')
    for row in csv.reader(open('Ucheniki.csv',encoding='utf-8'),delimiter=';'):
        if name.capitalize() in row:
            if family.capitalize() in row:
                a = row[0]
                b  = True
        else:
            b = False
    
    if  b == False:
        print('К сожалению такого ученика не найдено в нашей базе')
        
    else:
        with open('search.csv', 'w',encoding='utf-8') as out: 
            for row in csv.reader(open('Roditeli.csv',encoding='utf-8'),delimiter=';'):
                if a in row:
                    file_writer = csv.writer(out, delimiter = ',', lineterminator="\r")
                    file_writer.writerow (row[1:])

