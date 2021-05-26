import logger_path
import json
import logging
from client_path_settings import default_path
import os

logger = logging.getLogger('__name__')  # подключаем логирование


def auth(name: str, password: str):
    while True:
        with open(os.path.abspath(r'../auth.json'), 'r') as f:  # читаем json файл с данными пользователей
            information = json.load(f)

        for i in range(len(information)):  # проверяем, есть ли введеный пароль и логин в файле json
            if information[i][0] == name and information[i][1] == password:
                logger.info(f'Добро пожаловать {information[i][0]} {information[i][1]}')
                return default_path(information[i][0])
            elif information[i][0] == name and information[i][1] != password:
                logger.info('Неверный пароль')
                return False

        with open('../auth.json', 'w') as f:  # если пароля и логина нет в списке,то добавляем
            information.append([name, password])
            json.dump(information, f)
        logger.info(f'Учетная запись {name} {password} создана')
        return default_path(name)  # создаем папку для пользователя
