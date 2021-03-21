import RPi.GPIO as GPIO

pin = 7

def led_off():
    print("Apagando...")
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Main
while True:
    print("Iniciando...")
    led_off()