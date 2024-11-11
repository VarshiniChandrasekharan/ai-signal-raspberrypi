import gpiozero
from time import sleep

#led = gpiozero.LED(17)
#led.on()

segment_a = gpiozero.LED(2)
digit_1 = gpiozero.LED(6)

print(f"segment a value: {segment_a.value}")
print(f"display 1 value: {digit_1.value}")

def test_segment_a():
    digit_1.on()

    segment_a.on()
    print(f"segment a value: {segment_a.value}")
    print(f"display 1 value: {digit_1.value}")

    sleep(3)

    segment_a.off()

    digit_1.off()
    print(f"segment a value: {segment_a.value}")
    print(f"display 1 value: {digit_1.value}")

    # led.off()

if __name__ == "__main__":
    try:
        test_segment_a()
    except KeyboardInterrupt:
        pass
    finally:
        segment_a.off()
        digit_1.off()