from tello3 import Tello
import time
def start():
    tello = Tello()
    
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
                tello.send_command(message)
        with open(f"log/{time.time()}.log","w") as file:
            log = tello.get_log()
            for i in log:
                i.print_stats()
                file.write(i.return_stats())
            
    except Exception:
        print("Exception")
        sock.close()
        exit()
        
if __name__=="__main__":
    start()