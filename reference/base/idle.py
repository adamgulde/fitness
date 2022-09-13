from random import random
import mouse
import screeninfo
screen_width, screen_height = 0, 0
for monitor in screeninfo.get_monitors():
    screen_width = monitor.width
    screen_height = monitor.height
    break

def idle():
    print('IDLE: Starting idle mouse movement!')
    while(True):
        rand_dist = random()*100
        method = int(random()*3)
        if method==0: worm(rand_dist)
        if method==1: spiral(rand_dist) 
        if method==2: diamond_infinity(rand_dist)
        mouse.move(screen_width/2, screen_height/2, duration=1)
        with open('cmds.txt') as cmds:
            cmd = cmds.readline()
            if(cmd!='idle'):
                break
    print('IDLE: Ended idle mouse movement!')
        
    
def diamond_infinity(size :int):
    for _ in range(int(random()*10)):
        mouse.move(size, -size, False, duration=0.1)
        mouse.move(size, size, False, duration=0.1)
        mouse.move(-size, size, False, duration=0.1)
        mouse.move(-size, -size, False, duration=0.1)
        mouse.move(-size, -size, False, duration=0.1)
        mouse.move(-size, size, False, duration=0.1)
        mouse.move(size, size, False, duration=0.1)
        mouse.move(size, -size, False, duration=0.1)
        with open('cmds.txt') as cmds:
            cmd = cmds.readline()
            if(cmd!='idle'):
                break

def spiral(size:int):
    dist = 5
    while dist < size:
        mouse.move(dist, 0, False, 0.1)
        mouse.move(0, dist, False, 0.1)
        dist += 3
        mouse.move(-dist, 0, False, 0.1)
        mouse.move(0, -dist, False, 0.1)
        dist += 3
        with open('cmds.txt') as cmds:
            cmd = cmds.readline()
            if(cmd!='idle'):
                break

def worm(size:int):
    for movement_index in range(int(random()*50)):
        dir = int(random()*4)
        if dir == 0 and mouse.get_position()[1] > 200: mouse.move(0, -size, False, 0.1)
        if dir == 1 and mouse.get_position()[0] < screen_width - 200: mouse.move(size, 0, False, 0.1)
        if dir == 2 and mouse.get_position()[1] < screen_height - 200: mouse.move(0, size, False, 0.1)
        if dir == 3 and mouse.get_position()[0] > 200: mouse.move(-size, 0, False, 0.1)
        with open('cmds.txt') as cmds:
            cmd = cmds.readline()
            if(cmd!='idle'):
                break

if __name__ == "__main__":
    mouse.move(screen_width/2, screen_height/2, duration=1)
    idle()