import os
from shutil import copyfile, move, rmtree, copy2


class FileManager:
    pathway = False
    head_directory_name = False

    def set_pathway(self, path):
        self.pathway = path
        self.head_directory_name = os.path.split(self.pathway)[1]

    def get_pathway(self):
        return self.pathway

    def get_head_directory_name(self):
        return self.head_directory_name

    def create_directory(self, name):
        if os.path.isdir(fr'{os.path.join(self.pathway, name)}') is False:
            os.mkdir(f"{os.path.join(self.pathway, name)}")
            dir_way = os.path.join(self.pathway, name)
            return f'{dir_way} - создан'
        else:
            return f'Папка уже создана'

    def remove_directory(self, name):
        files = os.listdir(f'{os.path.join(self.pathway, name)}')
        if len(files) > 0:
            rmtree(f'{os.path.join(self.pathway, name)}')
            return f'папка {name} удалена рекурсивным методом'
        else:
            os.rmdir(f"{os.path.join(self.pathway, name)}")
            return f'папка {name} удалена'

    def move_in_path(self, name):
        if os.path.isdir(f'{os.path.join(self.pathway, name)}'):
            self.pathway = fr'{os.path.join(self.pathway, name)}'
            return self.pathway
        else:
            return 'Папка не существует'

    def move_up(self):
        if os.path.split(self.pathway)[1] != self.head_directory_name:
            self.pathway = os.path.split(self.pathway)[0]
            return self.pathway
        else:
            return "Переместиться выше нельзя"

    def create_file(self, name):
        file_name = os.path.join(self.pathway, name)
        if os.path.isfile(fr'{os.path.join(self.pathway, name)}') is False:
            file = open(fr'{file_name}', 'w')
            file.close()
            return f'{file_name} создан'
        else:
            return f'Файл {name} уже существует'

    def write_file(self, name, text):
        file = os.path.isfile(os.path.join(self.pathway, name))
        if file:
            with open(os.path.join(self.pathway, name), 'w') as f:
                f.write(text)
            return f'в файл {name} записан текст'
        else:
            return f'Файл {name}не существует'

    def read_file(self, name):
        file = os.path.isfile(os.path.join(self.pathway, name))
        if file:
            with open(os.path.join(self.pathway, name), 'r') as f:
                read = f.read()
            return read if len(read) > 0 else 'файл пуст'
        else:
            return f"Файл {name} не существует"

    def delete_file(self, name):
        file = os.path.isfile(os.path.join(self.pathway, name))
        if file:
            os.remove(os.path.join(self.pathway, name))
            return f'Файл {os.path.join(self.pathway, name)} удален'
        return f'Файл {name} не существует'

    def copy_file(self, name, to):
        directory = os.path.isdir(os.path.join(self.pathway, os.path.split(to)[0]))
        file = os.path.isfile(os.path.join(self.pathway, name))
        if file and directory:
            copyfile(os.path.join(self.pathway, name), os.path.join(self.pathway, to))
            return f"Файл {os.path.join(self.pathway, name)} копирован в {os.path.join(self.pathway, to)}"
        elif file is False:
            return f"Файл {name} не найден"
        else:
            return f"Директория {to} не найдена"

    def move_file(self, name, to):
        directory = os.path.isdir(os.path.join(self.pathway, os.path.split(to)[0]))
        file = os.path.isfile(os.path.join(self.pathway, name))
        if file and directory:
            move(os.path.join(self.pathway, name), os.path.join(self.pathway, to))
            return f"Файл {os.path.join(self.pathway, name)} перемещен в {os.path.join(self.pathway, to)}"
        elif file is False:
            return f"Файл {os.path.join(self.pathway, name)} не найден"
        else:
            return f"Директория {os.path.join(self.pathway, to)} не найдена"

    def rename_file(self, name, to):
        file = os.path.isfile(os.path.join(self.pathway, name))
        if file:
            os.rename(os.path.join(self.pathway, name), os.path.join(self.pathway, to))
            return f"Файл {os.path.join(self.pathway, name)} переименован в {os.path.join(self.pathway, to)}"

    def get_pwd(self):
        return self.pathway

    def show_list(self, path=None):
        return f'Содержимое текущей дериктории: {", ".join(os.listdir(self.pathway))}' if path is None else f'Содержимое директории: {", ".join(os.listdir(os.path.join(self.pathway, path)))}'

    def download_file(self, from_f, to_f):
        directory = os.path.isdir(os.path.join(self.pathway, os.path.split(to_f)[0]))
        file = os.path.isfile(os.path.join(from_f))
        if file and directory:
            copy2(os.path.join(from_f), os.path.join(self.pathway, to_f))
            return f"Файл {os.path.join(from_f)} загружен в {os.path.join(self.pathway, to_f)}"
        elif file is False:
            return f"Файл {os.path.join(from_f)} не найден"
        else:
            return f"Директория {os.path.join(self.pathway, to_f)} не найдена"

    def send_file(self, from_f, to_f):
        directory = os.path.isdir(os.path.join(os.path.split(to_f)[0]))
        file = os.path.isfile(os.path.join(self.pathway, from_f))
        if file and directory:
            copy2(os.path.join(self.pathway, from_f), os.path.join(to_f))
            return f"Файл {os.path.join(self.pathway, from_f)} отправлен в {os.path.join(to_f)}"
        elif file is False:
            return f"Файл {os.path.join(self.pathway, from_f)} не найден"
        else:
            return f"Директория {os.path.join(to_f)} не найдена"
