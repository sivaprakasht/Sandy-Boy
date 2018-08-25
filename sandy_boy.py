print('Sandy Body Starting...')
from gpiozero import Robot
from bluedot import BlueDot
import time


robo = Robot(right=(7,8), left=(20,21))

def move(pos):    
    if pos.top:
        print('Forward ^')
        robo.forward()
    elif pos.bottom:
        print('backward V')
        robo.backward()
    elif pos.right:
        print('Right ->')
        robo.right()
    elif pos.left:
        print('Left <-')
        robo.left()

def halt():
    print('Stopped !')
    robo.stop()

bd = BlueDot()
bd.wait_for_press()
bd.when_pressed = move
bd.when_moved = move
bd.when_released = halt

print('Ready for action !')

        
        
    
