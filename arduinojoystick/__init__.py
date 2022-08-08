from . import joystick
from . import board
device = None
joystick_ = None
def init(board_file, vrx, vry, sw):
    global joystick_
    device = board.device(board_file, vrx, vry, sw)
    device.init()
    joystick_ = joystick.joystick(device)
def get(n):
    return joystick_.input(n)