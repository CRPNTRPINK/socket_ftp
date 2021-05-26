import unittest
import socket
import logger_path
import logging
import sys
from socket_path.auth import auth

logger = logging.getLogger()
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)


class TestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(('localhost', 9002))

    def tearDown(self) -> None:
        self.client.close()

    def test_pwd(self):
        auth_result = auth('unit', 'unit')
        command = f'{auth_result}: pwd'.encode()
        self.client.send(command)
        logger.info(command)
        self.assertEqual(self.client.recv(1024).decode().split('/')[5],
                         'FTP')

        command = f'{auth_result}: create -d test_package'.encode()
        self.client.send(command)
        logger.info(command)
        self.assertEqual(self.client.recv(1024).decode().split('-')[1].strip(), 'создан')

        command = f'{auth_result}: move in test_package'.encode()
        self.client.send(command)
        logger.info(command)
        self.assertEqual(self.client.recv(1024).decode().split('/')[-1], 'test_package')

        command = f'{auth_result}: move up'.encode()
        self.client.send(command)
        logger.info(command)
        self.assertTrue(self.client.recv(1024).decode())

        command = f'{auth_result}: remove -d test_package'.encode()
        self.client.send(command)
        logger.info(command)
        self.assertEqual(self.client.recv(1024).decode().split(' ')[2], 'удалена')

        command = f'{auth_result}: create -f unit.txt'.encode()
        self.client.send(command)
        logger.info(command)
        self.assertEqual(self.client.recv(1024).decode().split(' ')[1], 'создан')

        command = f'{auth_result}: write -f unit.txt hello'.encode()
        self.client.send(command)
        logger.info(command)
        self.assertEqual(self.client.recv(1024).decode(), 'в файл unit.txt записан текст')

        command = f'{auth_result}: read -f unit.txt'.encode()
        self.client.send(command)
        logger.info(command)
        self.assertEqual(self.client.recv(1024).decode(), 'hello')

        command = f'{auth_result}: remove -f unit.txt'.encode()
        self.client.send(command)
        logger.info(command)
        self.assertEqual(self.client.recv(1024).decode().split(' ')[2], 'удален')


if __name__ == '__name__':
    unittest.main()
