import pyfirmata

from frames.variables import BayEight
import time
board = pyfirmata.Arduino('COM6')
BayTwo=board.get_pin('d:3:p')
while 1:
    BayTwo.write(0.5)
    time.sleep(1)
    BayTwo.write(0)
    time.sleep(1)