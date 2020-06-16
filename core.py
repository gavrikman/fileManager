# Консольный файловый менеджер.
import os
import shutil
import datetime
import os.path


def end_command():
    print('Done')


def create_file(name, text=None, extension='.txt'):
    def create_confirm():
        with open(name + extension, 'w', encoding='utf-8') as f:
            if text:
                f.write(text)
        end_command()

    if os.path.exists(name + extension) and os.path.isfile(name + extension):
        check = input(f'Файл {name + extension} уже существует. Заменить файл? Y/N: ')
        if check == 'Y' or check == 'y':
            create_confirm()
        else:
            return print('Выполнение создания прервано пользователем')
    else:
        create_confirm()


def create_folder(name):
    try:
        os.mkdir(name, 0o777)  # создаем папку
    except FileExistsError:
        print('Такая папка уже есть')
    else:
        end_command()


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)
    end_command()


def delete(name):
    try:
        if not os.path.exists(name):
            raise FileNotFoundError
    except FileNotFoundError:
        print(f'Не удалось найти указанный файл/папку: {name}')
    else:
        if os.path.isdir(name):
            os.rmdir(name)
        else:
            os.remove(name)
        end_command()


def copy_file(name, new_name):
    def copy_file_confirm():
        shutil.copy(name, new_name)
        end_command()

    try:
        if not os.path.exists(name):
            raise FileNotFoundError
        if name == new_name:
            raise shutil.SameFileError
    except FileNotFoundError:
        print(f'Не удалось найти копируемый файл/папку: {name}')
    except shutil.SameFileError:
        print('Наименования нового элемента должно отличаться')
    else:
        if os.path.isdir(name):  # если папка
            try:
                shutil.copytree(name, new_name)
            except FileExistsError:
                print('Такая папка уже есть. Нельзя заменить папку.')
            else:
                end_command()
        else:  # если файл
            if os.path.exists(new_name) and os.path.isfile(name):
                check = input('Файл уже существует. Заменить файл? Y/N: ')
                if check == 'Y' or check == 'y':
                    copy_file_confirm()
                else:
                    return print('Выполнение копирования прервано пользователем')
            else:
                copy_file_confirm()


def change_dir(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print('Директория не найдена')
    else:
        end_command()
        print('Текущая директория: ', os.getcwd())


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    os.path.join(os.getcwd(), 'log.txt')
    with open(os.path.join(os.getcwd(), 'log.txt'), 'a', encoding='utf-8') as f:
        f.write(result + '\n')
