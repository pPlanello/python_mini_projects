from smbus import SMBus

"""

> i2cdetect -y 1  # to detect address

"""

# Variables

i2c = SMBus(1)
address = 0x68

while True:
    bus_data = i2c.read_i2c_block_data(address, 0, 0x16)
    print(bus_data)