import math

'''
Class that hold all user informations and input, like position and pressed keys.
'''
class Camera:
    x = 0
    y = 2
    z = -10
    frameCount = 0
    yaw = 0
    pitch = 0
    zPressed = False
    qPressed = False
    sPressed = False
    dPressed = False
    upPressed = False
    downPressed = False
    leftPressed = False
    rightPressed = False

cam = Camera()