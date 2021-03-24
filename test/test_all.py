from smbus import SMBus
import RPi.GPIO as GPIO

# GPIO 04 = 1-Wire (PUF)
# I2C -> 2476 (Validador)
# Conexion UART

# Variables
PIN_LED = 29 # GPIO 05 = LED

GPIO_1WIRE = 4

I2C_ADDRESS = 0x3b #[7 bits] 011 1011
DEVICE_REG_MODE1 = 0x00
I2C = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
RNG_DS2476 = 0xd2


def testing_led():
    """
        Method that test LED
    """
    print("Testing LED...")
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(PIN_LED, GPIO.OUT)
        GPIO.output(PIN_LED, GPIO.HIGH)
    except:
        print(" **** Error in LED Test **** ")

def testing_i2c_read():
    """
        Method that test read I2C
    """
    print("Testing read I2C...")
    try:
        # Getting random value
        bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG_MODE1, RNG_DS2476)
        data_i2c = read_i2c_block_data(address, DEVICE_REG_MODE1, 0x16)
        print(data_i2c)
    except:
        print(" **** Error in read I2C Test **** ")


def __name__ == "__main__":
    print("Testing board...")
    while True:
        testing_led()
        testing_i2c_read()
    
