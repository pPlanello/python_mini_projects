import RPi.GPIO as GPIO
from time import sleep

# Variables
pin_led = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_led, GPIO.OUT)
GPIO.output(pin_led, GPIO.LOW)

def led_on():
    print("Encendiendo")
    GPIO.output(pin_led, GPIO.HIGH)
    sleep(0.5)
    print("Apagando")
    GPIO.output(pin_led, GPIO.LOW)
    sleep(0.5)

# Main
while True:
    print("Iniciando")
    led_on()
    sleep(1)