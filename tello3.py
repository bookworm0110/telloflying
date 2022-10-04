import socket, threading, time
from stats import Stats
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
        self.log.append(Stats(command,len(self.log)))
        self.socket.sendto(command.encode("utf-8"),self.tello_address)
        start=time.time()
        print(f"Sending command {command}")
        if command.startswith("rc"):
            print(f"Sent command {command}")
        else:
            while not self.log[-1].got_response():
                now=time.time()
                diff=now-start
                if diff>self.MAX_TIMEOUT:
                    print("Timed Out, Exiting")
                    socket.close()
                    end()
            print(f"Sent command {command}, {diff} seconds elapsed")
    def receive_thread(self):
        while True:
            try:
                self.response, ip=self.socket.recvfrom(1024)
                print(f"from {ip}: {self.response}")
                self.log[-1].add_response(self.response)
            except Exception as exec:
                print(f"Socket error: {exec}")
    def land(self):
        self.send_command("land")
    def get_log(self):
        return self.log
    def takeoff(self):
        self.send_command("takeoff")
    
        