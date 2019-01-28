import easy
import os

def folder_actions():
    """
Функция выполняет действия над директориями
в соответствии с запросами пользователя
    """
    user_request = 'a'
    while user_request != '0':
        print(""" Введите:
'1' для перехода в указанную директорию
'2' для просмотра содержимого текущей директории
'3' для удаления указанной директории
'4' для создания директории""")
        user_request = input()

        if user_request == '1':
            dir_name = input('введите название директории для перехода: ')
            easy.change_dir(dir_name)
            print ('Выберите дальнейшие действия')
        elif user_request == '2':
                dir_name = os.getcwd()
                easy.list_dir(dir_name)
        elif user_request == '3':
                dir_name = input('введите имя удаляемой директории: ')
                easy.delete_dir(dir_name)
        elif user_request == '4':
                dir_name = input('задайте имя создаваемой директории: ')
                easy.make_dir(dir_name)
        elif type(user_request) is not int or len(user_request) >= 1:
            print('неверная команда меню')
print (folder_actions())