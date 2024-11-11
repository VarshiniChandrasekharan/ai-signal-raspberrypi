import gpiozero
from time import sleep

pin_2 = gpiozero.LED(2)
pin_2.active_high = True
sleep(100)