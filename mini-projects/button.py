from fysom import Fysom # Library maquina estados
from gpiozero import LED
from gpiozero import Button
from time import sleep

button = Button(17)

while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button not pressed")
