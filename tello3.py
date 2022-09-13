import socket, threading, time
class Tello(object):
    def __init__(self):
        self.socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind("", 8889)
        #start recieving thread
        self.recieve_thread=threading.Thread(target=self.recieve_thread,daemon=True)
        self.recieve_thread.start()
        self.tello_address = ("192.168.10.1", 8889)
        self.log=[]
        self.MAX_TIMEOUT=15
        self.socket.sendto(b"command", "192.168.10.1")
    def send_command(self, command):
        pass
    def recieve_thread(self):
        pass
