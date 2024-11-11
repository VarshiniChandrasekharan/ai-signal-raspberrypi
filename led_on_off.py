import gpiozero
from gpiozero import LED
from time import sleep
import urllib.request
import json

'''pin_4 = gpiozero.LED(4)
pin_17 = gpiozero.LED(17)
pin_0 = gpiozero.LED(0)
pin_27 = gpiozero.LED(27)
pin_22 = gpiozero.LED(22)
pin_10 = gpiozero.LED(10)
pin_9 = gpiozero.LED(9)
pin_11 = gpiozero.LED(11)

pin_4.on()
pin_17.on()
pin_27.off()
pin_0.on()
pin_22.on()
pin_10.on()
pin_9.on()
pin_11.on()

sleep(3)

pin_4.off()
pin_17.off()
pin_27.on()
pin_0.off()
pin_22.off()
pin_10.off()
pin_9.off()
pin_11.off()'''

segments1 = {
    'a': LED(17),
    'b': LED(27),
    'c': LED(22),
    'd': LED(10),
    'e': LED(9),
    'f': LED(11),
    'g': LED(0)
}

segments2 = {
    'a': LED(15),
    'b': LED(18),
    'c': LED(23),
    'd': LED(24),
    'e': LED(25),
    'f': LED(8),
    'g': LED(7)
}

ground1 = LED(4)

ground2 = LED(14)

numbers = {
    '0': ['a', 'b', 'c', 'd', 'e', 'f'],
    '1': ['b', 'c'],
    '2': ['a', 'b', 'd', 'e', 'g'],
    '3': ['a', 'b', 'c', 'd', 'g'],
    '4': ['b', 'c', 'f', 'g'],
    '5': ['a', 'c', 'd', 'f', 'g'],
    '6': ['a', 'c', 'd', 'e', 'f', 'g'],
    '7': ['a', 'b', 'c'],
    '8': ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    '9': ['a', 'b', 'c', 'd', 'f', 'g']
}



def display_number(number1, number2):
    ground1.on()
    ground2.on()

    # print(f"number1, number2: {number1} {number2}")

    segment_of_numbers1 = numbers[str(number1)]
    segment_of_numbers2 = numbers[str(number2)]


    for segment in segments1:
        if segment in segment_of_numbers1:
            # print(f'segment {segment} off')
            segments1[segment].off()
        else:
            # print(f'segment {segment} on')
            segments1[segment].on()

    for segment in segments2:
        if segment in segment_of_numbers2:
            # print(f'segment {segment} off')
            segments2[segment].off()
        else:
            # print(f'segment {segment} on')
            segments2[segment].on()
    
    sleep(1)
    
    ground1.off()
    ground2.off()

    for segment in segments1:
        segments1[segment].on()

    for segment in segments2:
        segments2[segment].on()


url = "http://feswai-ip-223-178-84-101.tunnelmole.net/get-traffic-status"

traffic_status = ""

ground_red = LED(26)
led_red = LED(20)
ground_green = LED(13)
led_green = LED(21)

while True:
    with urllib.request.urlopen(url) as response:
        if response.status == 200:
            data = json.loads(response.read().decode())
            print(data)
            traffic_status = data.get('trafficStatus')
            print(f"Traffice Status: {traffic_status}")
        else:
            print(f"Failed to retrieve traffic status.")

    green_duration = 20

    if (traffic_status == 'low'):
        green_duration = 20
    elif (traffic_status == 'medium'):
        green_duration = 40
    elif (traffic_status == 'high'):
        green_duration = 60

    if (green_duration > 0):
        ground_green.off()
        led_green.on()
        ground_red.on()
        led_red.off()
        for i in range(green_duration, -1, -1):
            green_duration -= 1
            number_str = str(i)
            if (len(number_str) == 2):
                first_digit = int(number_str[0])
                second_digit = int(number_str[1])
                display_number(second_digit, first_digit)
            else:
                display_number(i, 0)
        ground_green.on()
        led_green.off()
        ground_red.off()
        led_red.on()
        for i in range(60, -1, -1):
            green_duration -= 1
            number_str = str(i)
            if (len(number_str) == 2):
                first_digit = int(number_str[0])
                second_digit = int(number_str[1])
                display_number(second_digit, first_digit)
            else:
                display_number(i, 0)
