from tools import logger1, logger2

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

@logger1
def name_of_doc_owner(docs, num):
    '''
    Функция поиска владельца документа по номеру.
    Проходим по словарям, находим совпадающее с введённым значение по ключу number.
    Возвращаем имя владельца. Если не находим такой номер - сообщаем пользователю об этом.
    '''
    for doc in docs:
        if doc["number"] == num:
            return f'Владелец этого документа - {doc["name"]}'
    return "Такого документа не существует!"

@logger1
def number_of_shelf(shelves, num):
    '''
    Функция поиска номера полки, на которой лежит документ.
    Проходим по спискам (значениям словаря) поэлементно, если находим соответствующий номер - возвращаем данный ключ (номер полки).
    '''
    for shelf, numbers in shelves.items():
        for number in numbers:
            if num == number:
                return f'Этот документ находится на полке №{shelf}'
    return "Этот документ не лежит ни на одной из полок!"

@logger1
def list_of_docs(docs):
    '''
    Функция вывода каталога документов в формате: type "number" "name".
    Итерируя по элементам списка (словарям), выводим значения ключа type, все остальные значения выводим в двойных кавычках.
    '''
    for doc in docs:
        for type, value in doc.items():
            if type == 'type':
                print(value, end=' ')
            else:
                print(f'"{value}"', end=' ')
        print()

@logger1
def add_document(docs, shelves, doctype, num, name):
    '''
    Функция добавления документа.
    Получает на вход каталог документов, полок, тип документа, номер, имя владельца.
    До тех пор пока пользователь не введет номер существующей полки, будет действовать бесконечный цикл.
    Создаём новый словарь с данными о документе.
    Добавляем новый словарь в каталог документов, а номер документа на введенную полку.
    '''
    while True:
        shelf_in = input('Введите номер полки, на которой будет храниться документ: ')
        if shelf_in not in shelves.keys():
            print('Такой полки не существует!')
        else:
            break
    new_doc = {"type": doctype, "number": num, "name": name}
    docs.append(new_doc)
    shelves[shelf_in].append(num)
    print(f'Документ будет храниться на полке №{shelf_in}')

@logger1
def delete_document(docs, shelves, num):
    '''
    Функция удаления документа.
    Сначала находим по номеру документ в каталоге документов. Удаляем его.
    После этого находим номер документа на полках и удаляем его. Прерываем функцию.
    Если функция не прервется, т.е. документ не был найден, сообщаем пользователю об этом.
    '''
    for i in range(len(docs)):
        if docs[i]["number"] == num:
            del docs[i]
            break

    for shelf in shelves.values():
        for i in range(len(shelf)):
            if shelf[i] == num:
                del shelf[i]
                print(f"Документ с номером '{num}' удалён")
                return
    
    print('Невозможно удалить несуществующий документ!')
    
@logger1
def move_doc_between_shelves(shelves):
    '''
    Функция перемещения документа с одной полки на другую.
    Если введенная полка-назначение не существует, прерываем функцию.
    Проверяем есть ли такой документ на полках. Находим номер на полках, удаляем его оттуда. После этого добавляем на новую полку.
    Если функция не была прервана, значит документ не найден.
    '''
    new_shelf = input('На какую полку переместить: ')
    
    if new_shelf not in shelves.keys():
        print('Такой полки не существует!')
        return
    num = input('Введите номер документа: ')
    for shelf, numbers in shelves.items():
        if num in numbers:
            shelves[shelf].remove(num)
            shelves[new_shelf].append(num)
            print(f'Документ перемещен на полку {new_shelf}')
            return
    print('Документ не найден!')

@logger1
def add_shelf(shelves, position):
    '''
    Функция добавления полки.
    Если пользователь пытается добавить полку с существующим номером, программа не даст ему этого сделать. Функция прервётся.
    Если номер не зарезервирован - создаем новый элемент словаря {номер_полки: пустой список}
    '''
    if position in shelves:
        print('Полка с таким номером уже зарезервирована!')
        return
    else:
        shelves[position] = []
        print(f'Добавлена полка под номером {position}')

@logger1
def main_function(shelves):
    '''
    Основная функция.
    Вызываются все остальные функции, в зависимости от команды которую введет пользователь.
    p - поиск владельца документа по номеру.
    s - поиск номера полки, на которой лежит документ
    l - вывод каталога документов в формате: type "number" "name"
    a - добавление документа
    d - удаление документа
    m - перемещение документа с одной полки на другую
    as - добавление полки
    q - завершение программы
    Все прочие команды выведут сообщение о повторной попытке ввода.
    '''
    while True:
        request = input('Введите команду: ')
        if request == 'p':
            print(name_of_doc_owner(documents, input('Введите номер документа: ')))
        elif request == 's':
            print(number_of_shelf(directories, input('Введите номер документа: ')))
        elif request == 'l':
            list_of_docs(documents)
        elif request == 'a':
            name_in = input('Введите имя владельца документа: ')
            number_in = input('Введите номер документа: ')
            type_in = input('Введите тип документа: ')
            add_document(documents, directories, type_in, number_in, name_in)
        elif request == 'd':
            delete_document(documents, directories, input('Введите номер документа для удаления: '))
        elif request == 'm':
            move_doc_between_shelves(directories) 
        elif request == 'as':
            add_shelf(shelves, input('Введите номер новой полки: '))
        elif request == 'q':
            break
        else:
            print('Неизвестная команда, попробуйте снова!')

#Вызываем основную функцию после объявления всех функций
main_function(directories)


