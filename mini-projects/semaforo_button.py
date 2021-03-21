from fysom import Fysom # Library maquina estados
from gpiozero import LED
from gpiozero import Button
from time import sleep

# Variables
state = Fysom({ 'initial': 'green',
                'events': [
                    {'name': 'precaucion', 'src': 'green', 'dst': 'yellow'}, 
                    {'name': 'stop', 'src': 'yellow', 'dst': 'red'},
                    {'name': 'go', 'src': 'red', 'dst': 'green'},
                    {'name': 'wait_green', 'src': 'green', 'dst': 'green'},
                    {'name': 'wait_yellow', 'src': 'yellow', 'dst': 'yellow'},
                    {'name': 'wait_red', 'src': 'red', 'dst': 'red'}
                ]
            })

ledGreen = LED(2)
ledYellow = LED(3)
ledRed = LED(4)
button = Button(17)
debounce_time = 0.15

def green_led():
    print(state.current)
    ledGreen.on()
    ledYellow.off()
    ledRed.off()
    if button.is_pressed:
        sleep(debounce_time)
        print("Button is pressed")
        state.precaucion()


def yellow_led():
    print(state.current)
    ledGreen.off()
    ledYellow.on()
    ledRed.off()
    if button.is_pressed:
        sleep(debounce_time)
        print("Button is pressed")
        state.stop()

def red_led():
    print(state.current)
    ledGreen.off()
    ledYellow.off()
    ledRed.on()
    if button.is_pressed:
        sleep(debounce_time)
        print("Button is pressed")
        state.go()
    
def event_button_not_pressed():
    if state.current == "green":
        green_led()
    if state.current == "yellow":
        yellow_led()
    if state.current == "red":
        red_led()

def event_button_pressed():
    print("Pulsando boton")
    print(state.current)
    if state.current == "green":
        state.precaucion()
    if state.current == "yellow":
        state.stop()
    if state.current == "red":
        state.go()

print("Iniciando...")
# Main
while True:
    sleep(debounce_time)
    if state.current == "green":
        green_led()
    if state.current == "yellow":
        yellow_led()
    if state.current == "red":
        red_led()
    