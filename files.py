def fileopen():
    file=open("test.txt","w")
    try:
        file.write("this is a test message. change this in files.py")
    finally:
        file.close()
def fileopenwith():
    with open("testwith.txt","w") as file:
        file.write("this is a test message. change this in files.py")
def fileread():
    with open("command.txt","r") as file:
        commands=file.readlines()
        for command in commands:
            print(command)

if __name__=="__main__":
    fileread()