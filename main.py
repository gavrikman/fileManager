import sys
import os
from core import create_file, create_folder, get_list, delete, copy_file, save_info, change_dir


def info():
    print('Неверный формат ввода. Повторите команду')
    print('Для получения списка команд и формата ввода, введите "help"')


save_info('Start')

try:
    command = sys.argv[1]
except IndexError:
    print('Укажите команду')
    print('Для получения списка команд, введите "help"')
else:
    if command == 'list':
        text = None
        while text != 1 or text != 2:
            try:
                text = int(input('Для вывода списка всех файлов и папок директории, введите 1. '
                                 'Для вывода только списка папок, введите 2: '))
            except ValueError:
                print('Неверный формат ввода')
            else:
                if text == 1:
                    get_list()
                elif text == 2:
                    get_list(True)
                break

    ##################################################################
    elif command == 'create_file':
        def file_name():  # функция определения имени файла и расширешия
            dots = [name.index(i) for i in name if i == '.']  # если есть точка в имени, считаем, что указано расширешие
            return name[0:dots[0]] if dots else name  # присваиваем имя

        def file_extension():  # функция определения имени файла и расширешия
            dots = [name.index(i) for i in name if i == '.']  # если есть точка в имени, считаем, что указано расширешие
            return '.' + name[(dots[0] + 1):] if dots else '.txt'  # присваиваем расширение

        try:
            name = sys.argv[2]
        except IndexError:
            info()
        else:
            text = input('Введите текст (если не требуется, введите N): ')
            if text == 'N' or text == 'n':
                create_file(file_name(), None, file_extension())
            else:
                create_file(file_name(), text, file_extension())

    ##################################################################
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            info()
        else:
            create_folder(name)
    ##################################################################
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            info()
        else:
            delete(name)
    ##################################################################
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            info()
        else:
            copy_file(name, new_name)
    ##################################################################
    elif command == 'change_dir':
        print('Текущая директория: ', os.getcwd())
        try:
            new_dir = sys.argv[2]
        except IndexError:
            info()
        else:
            change_dir(new_dir)
    ##################################################################
    elif command == 'help':
        print('Текущая директория: ', os.getcwd())
        print('Список функций:')
        print('list - список файлов и папок')
        print('create_file - создание файла. '
              'Формат ввода: create_file название_файла расширение_файла(по умолчанию, .txt)')
        print('create_folder - создание папки. '
              'Формат ввода: create_folder название_папки')
        print('delete - удаление папки или файла. '
              'Формат ввода: delete название_файла/папки')
        print('copy - копирование папки или файла. '
              'Формат ввода: copy название_копируемого_файла/папки название_нового_файла/папки')
        print('change_dir - смена рабочей директории'
              'Формат ввода: change_dir название_папки(если она находится в текущей директории)'
              ' или название_полного_пути_до_папки')
    else:
        info()


save_info('End')
