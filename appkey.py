from tello3 import Tello
import pygame
import time
def init():
    pygame.init()
    # while True:
    pygame.display.set_mode((400,400))
def keycontrol():
    # call init()
    init()
    # Instantiate Tello
    tello=Tello()
    tello.takeoff()
    # Whiile tru, we want to convert Key to RC
    while True:
        try:
            rc = convertkeytorc()
            # Send Command using "rc" and 4 array elements
            tello.send_command(f"rc {rc[0]} {rc[1]} {rc[2]} {rc[3]}")
            time.sleep(0.05)
        except KeyboardInterrupt:
            tello.land()
            break


    # Give 0.05 pause, so it can properly send the command

    # Handle KeyboardInterrup exception

def getKey(keyName):
    answer = False
    for event in pygame.event.get():
        pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        answer = True
    pygame.display.update()
    return answer
def convertkeytorc():
    lr,fb,ud,yv=0,0,0,0
    speed=50
    if getkey("RIGHT"):
        lr=speed
    if getKey("LEFT"):
        lr=-speed
    if getkey("w"):
        ud=speed
    if getkey("s"):
        ud=-speed
    if getkey("UP"):
        fb=speed
    if getkey("DOWN"):
        fb=-speed
    if getkey("d"):
        yv=speed
    if getkey("a"):
        yv=-speed
    return [lr,fb,ud,yv]
if __name__=="__main__":
    init()
    