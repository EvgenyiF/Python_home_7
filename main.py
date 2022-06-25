import add
import write
import find

choice = int(input('Выберите режим работы 1-добавить нового ученика и родителей; 2 - поиск родителей по ученику: '))
if choice == 1:
    print('ВВедите данные ученика.')
    text = add.get_data()
    file = 'Ucheniki.csv'
    write.writer(text,file)
    print('ВВедите данные родителей.')
    for i in range(2):
        text = add.get_data1()
        file = 'Roditeli.csv'
        write.writer(text,file)
if choice == 2:
    print('ВВедите данные ученика.')
    find.search()