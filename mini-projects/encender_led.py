import RPi.GPIO as GPIO

# Variables
pin = 7

def led_on():
    print("Encendiendo...")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

# Main
while True:
    print("Iniciando...")
    led_on()