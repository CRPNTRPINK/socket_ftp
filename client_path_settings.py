import os


def default_path(name):
    if name == 'SOA_ADMIN':
        pathway = '/'.join(os.getcwd().split('/')[0:-1]) + '/client_path'
        return pathway
    cwd = '/'.join(os.getcwd().split('/')[0:-1]) + '/client_path'  # находим путь к папке client_path
    pathway = os.path.join(cwd, name)  # указываем путь к папке с названием юзера
    if os.path.isdir(f'../client_path/{name}') is False:  # создаем директорию для юзера, если она не создана
        os.mkdir(f'{pathway}')
    else:
        print(f"Стандартная директория уже создана - {pathway}")  # предупреждаем, что она создана, если создана
    return pathway
