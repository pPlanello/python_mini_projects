from gpiozero import LED
from time import sleep

# Variabales
led = LED(4)

def led_on_off():
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)

# Programa principal
while True:
    led_on_off()