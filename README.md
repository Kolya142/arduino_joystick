# arduino_joystick
libs:

[
"pyfirmata"
]

# use:
frist:

"""
    
    import arduinojoystick as aj
    aj.init(board_port:str, vrx_analog:int, 
        vry_analog:int, sw_analog:int)
    

"""

use:

"""

    aj.get(0)  # get: vrx
    aj.get(1)  # get: vry
    aj.get(2)  # get: sw

"""

# example:
"""

    import arduinojoystick as aj
    aj.init("//./COM4", 2, 3, 0)
    while True:
        print(f'x: {aj.get(0)}, y: {aj.get(1)}, press: {aj.get(2)}')

"""