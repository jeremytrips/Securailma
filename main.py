from packages.serial.serialport import SerialPort

from packages.utils.pubsub import Subscriber


class Handler(Subscriber):

    def __init__(self):
        super().__init__()

    def update(self, type, message):
        print(message)



h = Handler()
s = SerialPort("COM6")
s.register(h)
while(1):
    pass
