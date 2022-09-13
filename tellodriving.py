import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tello_address = ("192.168.10.1", 8889)
sock.bind(("", 9000))
print("Initiating startup sequence.")
sock.sendto(b"command", 0, tello_address)
sock.sendto(b"sdk?", 0, tello_address)
sock.sendto(b"sn?", 0, tello_address)
sock.sendto(b"battery?", 0, tello_address)
tick = 0
while True:
    tick=tick+1
    if tick == 20:
        sock.sendto(b"battery?", 0, tello_address)
    try:
        data, ip = sock.recvfrom(1024)
    except KeyboardInterrupt:
        print("Exiting")
        sock.close()
        break