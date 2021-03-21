from fysom import Fysom # Library maquina estados
from gpiozero import LED
from time import sleep

# Variables
state = Fysom({ 'initial': 'green',
                'events': [
                    {'name': 'precaucion', 'src': 'green', 'dst': 'yellow'}, 
                    {'name': 'stop', 'src': 'yellow', 'dst': 'red'},
                    {'name': 'go', 'src': 'red', 'dst': 'green'}
                ]
            })

ledGreen = LED(2)
ledYellow = LED(3)
ledRed = LED(4)

def green_led():
    print(state.current)
    ledGreen.on()
    ledYellow.off()
    ledRed.off()
    sleep(1)
    state.precaucion()

def yellow_led():
    print(state.current)
    ledGreen.off()
    ledYellow.on()
    ledRed.off()
    sleep(1)
    state.stop()

def red_led():
    print(state.current)
    ledGreen.off()
    ledYellow.off()
    ledRed.on()
    sleep(1)
    state.go()

print("Iniciando...")
# Main
while True:
    if state.current == "green":
        green_led()
    if state.current == "yellow":
        yellow_led()
    if state.current == "red":
        red_led()
    
