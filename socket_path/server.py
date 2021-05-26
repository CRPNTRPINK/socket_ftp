import socket
import threading
import logger_path
import logging
from app import manager
from file_manager import FileManager

logger = logging.getLogger('__name__')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('localhost', 9002))
server.listen(10)
print("Сервер запущен")


def accept():
    while True:
        try:
            file_manager = FileManager()
            conn, addr = server.accept()
            logger.info(addr)
            threading.Thread(target=connect, args=[conn, addr, file_manager]).start()
        except Exception as ex:
            logger.exception(ex)


def connect(conn, addr, file_manager):
    print('connect: ', file_manager.get_pathway())
    while True:
        try:
            recv = conn.recv(1024).decode()
            client_path = recv.split(':')[0]
            client_message = recv.split(':')[1].strip()
            if recv:
                logger.info(f'{addr}: {recv}')
                print(file_manager.get_pathway())
                answer = manager(client_message, client_path,
                                 file_manager)
                conn.send(answer.encode())
            else:
                conn.close()
                logger.warning(f'{addr} отключился')
                break
        except Exception as ex:
            logger.exception(ex)
            conn.close()
            break


t = threading.Thread(target=accept).start()
