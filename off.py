import gpiozero
from time import sleep

segment_a = gpiozero.LED(2)
digit_1 = gpiozero.LED(6)

#segment_a.off()
#digit_1.off()
# segment_a.value = 0
# digit_1.value = 0
segment_a.toggle()
digit_1.toggle()

sleep(3)

# segment_a.on()
# digit_1.on()
# segment_a.value = 1
# digit_1.value = 1
segment_a.toggle()
digit_1.toggle()
