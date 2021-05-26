import socket
from auth import auth

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9002))

while True:  # при подключении к серверу пользователь должен ввести логин и пароль
    name = input('Введите имя: ')
    password = input('Введите пароль: ')

    auth_result = auth(name, password)
    if auth_result:
        break

while True:
    try:
        message = input('> ')  # ввод сообщений
        client.send(f'{auth_result}: {message}'.encode())  # отправляем путь к папке и сообщение клиента
        recv = client.recv(1024).decode()
        print(recv)
    except Exception as ex:
        client.close()
        break
