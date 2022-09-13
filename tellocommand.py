import socket, threading, time
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ("192.168.10.1", 8889)
sock.bind(("", 9000))
# def send(message):
#     sock.sendto(command, 0, tello_address)
def reciever():
    while True:
        try:
            data, ip = sock.recvfrom(1518)
            print("{}: {}".format(ip, data.decode(encoding='utf-8')))
        except KeyboardInterrupt:
           print("Exiting")
           sock.close()
           break
def broadcaster():
    
    filename = input("Enter a file name to read. (E.g: file.txt) ")
    with open(filename,"r") as file:
       commands=file.readlines()
   
    try:
        print("Got it. Reading commands...")
        for command in commands:
            print("Sending: "+ command)
            if command != '' and command!='\n':
                command=command.rstrip()

                message=command
                message=message.encode(encoding="utf-8")
                sock.sendto(message,tello_address)
                time.sleep(5)
    except Exception:
        print("Exception")
        sock.close()
        exit()
        
if __name__=="__main__":
    print("hello")
    reciever=threading.Thread(target=reciever)
    # broadcaster=threading.Thread(target=broadcaster)
    print("starting thread(s)")
    reciever.start()
    sock.sendto(b"command", 0, tello_address)
    broadcaster()
    # broadcaster.start()
    # sock.sendto(b"battery?", 0, tello_address)