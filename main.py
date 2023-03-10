import time
import storage
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

time.sleep(1)

keyboard = Keyboard(usb_hid.devices)

keycodetable = [Keycode.SPACE, Keycode.W, Keycode.A, Keycode.S, Keycode.D, Keycode.UP_ARROW, Keycode.DOWN_ARROW, Keycode.LEFT_ARROW, Keycode.RIGHT_ARROW]
GPs = [board.GP0,board.GP1,board.GP2,board.GP3,board.GP4, board.GP5,board.GP6,board.GP7,board.GP8]
buttonpressed = []
btns = []

for i in range(9):
    btns.append(digitalio.DigitalInOut(GPs[i]))
    btns[i].direction = digitalio.Direction.INPUT
    btns[i].pull = digitalio.Pull.UP
    buttonpressed.append(False)

while True:
    for i in range(9):
        if not buttonpressed[i]:
            if not btns[i].value: #it's connected
                keyboard.press(keycodetable[i])
                buttonpressed[i] = True
        elif btns[i].value:
            keyboard.release(keycodetable[i])
            buttonpressed[i] = False
