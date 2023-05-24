# # 1. Открывать файл (режим txt)
# # 2. Сохранить файл
# # 3. Показать все контакты
# # 4. Добавить контакт
# # 5. Найти контакт
# # 6. Изменить контакт
# # 7. Удалить контакт
# # 8. Выход

# Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.

import re

def open_file ():
    path = 'phones.txt'
    data = open(path, 'r',encoding='cp1251')
    for line in data:
        print(line)
    data.close()

def new_contact (text_input):
    data = open('phones.txt', 'a')
    data.writelines('\n')
    data.writelines(text_input)
    data.close()

def input_contact():
    contact = list()
    contact.append(str(input("Введите Фамилию, Имя, Отчество и номер телефона через пробел: ").split()))
    return contact


def search_contact (search_element):
    path ='phones.txt'
    data = open(path, 'r',encoding='cp1251')
    for line in data:
        if line.__contains__(search_element):
            print('Такая запись найдена')
            print(line)
            return(line)
    


def change_contact():
    search_element = str(input('Введите контакт, который нужно изменить, например фамилию: '))
    element = search_contact(search_element)
    print(element)
    temp_list = list(re.split(',|[|]|\'',element))
    save_list = list()
    save_list.append(temp_list[1]) #фамилия
    save_list.append(temp_list[4])#имя
    save_list.append(temp_list[7])#отечество
    save_list.append(temp_list[10])#номер.
    change_element = int(input("Что хотите поменять? \n 1 - Фамилию \n 2 - Имя \n 3 - Отчество \n 4 - Номер \n"))
    new_change = str(input(f"Старое значение {save_list[change_element-1]} введите новое значение: "))
    match (change_element):
        case 1:
            save_list.pop(0)
            save_list.insert(0,new_change)
        case 2:
            save_list.pop(1)
            save_list.insert(1,new_change)
        case 3:
            save_list.pop(2)
            save_list.insert(2,new_change) 
        case 4:
            save_list.pop(3)
            save_list.insert(3,new_change)
    

     
    print(save_list)
    new_contact(str(save_list))
    with open('phones.txt', "r",encoding='cp1251') as f:
        lines = f.readlines()
    if element in lines:
        lines.remove(element)
    with open('phones.txt', "w",encoding='cp1251') as f:
        f.writelines(lines)
    
    
def delete_contact ():
    search_element = str(input('Введите контакт, который нужно удалить, например фамилию: '))
    element = search_contact(search_element)
    print(element)
    with open('phones.txt', "r",encoding='cp1251') as f:
        lines = f.readlines()
    if element in lines:
        lines.remove(element)
        print("Запись удалена")
    with open('phones.txt', "w",encoding='cp1251') as f:
        f.writelines(lines)
    
    
def user_interface ():
    print ("1 - Показать все контакты")
    print ("2 - Добавить контакт")
    print ("3 - Найти контакт")
    print ("4 - Изменить контакт")
    print ("5 - Удалить контакт")
    print ("6 - Выход")
    command = int(input('Введите номер команды: '))
    return command 

command = 0
while command < 7:
    command = user_interface()
    
    match (command):
        case 1:
            print ('Все контакты \n')
            open_file()
            print('\n')
        case 2:
            print ('Добавление контакта \n')
            new_contact(input_contact())
            print('\n')
        case 3:
            print ('Поиск контакта \n')
            search_contact(str(input("Введите номер телефона для поиска: ")))
            print('\n')
        case 4:
            print ('Изменение контакта \n')
            change_contact()
            print('\n')
        case 5:
            print ('Удаление контакта \n')
            delete_contact()
            print('\n')
        case 6:
            exit("Пакеда")
        
