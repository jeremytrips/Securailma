from serial import Serial
from threading import Thread

from packages.utils.pubsub import Publisher

import constant


class SerialPort(Publisher):

    def __init__(self, port):
        super().__init__()
        self.__serial = Serial()
        self.__serial.baudrate = 9600
        self.__serial.port = port
        self.__readed = b""
        self.__running = True
        self.__read_thread = Thread(target=self.read)
        self.__read_thread.setDaemon(True)
        self.open()

    def read(self):
        while self.__running:
            if self.__serial.in_waiting:
                while self.__serial.in_waiting:
                    self.__readed += self.__serial.read(1)
                self._dispatch(constant.GOT_NEW_MESSAGE, self.__readed)
                self.__readed = b""


    def open(self):
        self.__serial.open()
        self.__read_thread.start()

    def close(self):
        self.__read_thread.is_alive()
        self.__serial.close()
        self.__running = False

    @property
    def message(self):
        return self.__readed
