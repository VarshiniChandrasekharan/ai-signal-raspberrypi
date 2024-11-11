from gpiozero import LED
from time import sleep

ground_red = LED(26)
led_red = LED(20)
ground_green = LED(13)
led_green = LED(21)

ground_red.off()
led_red.on()
ground_green.off()
led_green.on()

sleep(10)

ground_red.on()
led_red.off()
ground_green.on()
led_green.off()