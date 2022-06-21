from pickle import TRUE
from numpy import byte
import pyfirmata

board=pyfirmata.Arduino('COM11')
IR_pin = board.get_pin('a:5:i')
LED_pin = board.get_pin('d:13:o')

it = pyfirmata.util.Iterator(board)
it.start()
while TRUE:
    analog_value = IR_pin.read()
    analog_value=float(analog_value or 0)
    print(analog_value)
    if analog_value < 0.5:
        LED_pin.write(1)
    else:
        LED_pin.write(0)