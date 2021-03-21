from time import sleep
from smbus import SMBus

# Variables
debounce_time = 0.25

i2c = SMBus(1)
address = 0x68

i2c.write_byte_data(address, 0x2C, 0x0A)
i2c.write_byte_data(address, 0x2D, 0x08)
i2c.write_byte_data(address, 0x31, 0x08)

def calculate_value_axis(data0, data1):
    #Convert the data to 10-bits
    x = ((data1 & 0x03) * 256) + data0
    if x > 511:
        x -= 1024
    return x

def calculate_grades(axis):
    trans = 360/255
    return round(trans * axis, 2)

print("Iniciando...")
# Main
while True:
    byte = i2c.read_i2c_block_data(address, 10, 0x16)
    # print(byte)
    x_lsb = byte[0]
    x_msb = byte[1]
    y_lsb = byte[2]
    y_msb = byte[3]
    z_lsb = byte[4]
    z_msb = byte[5]
    x = calculate_value_axis(x_lsb, x_msb)
    y = calculate_value_axis(y_lsb, y_msb)
    z = calculate_value_axis(z_lsb, z_msb)
    print('X={0}, Y={1}, Z={2} \r'.format(calculate_grades(x), calculate_grades(y), calculate_grades(z)))
    # print('X={0}, Y={1}, Z={2} \r'.format(x_lsb, y_lsb, z_lsb))
    # print('X={0}, Y={1}, Z={2}'.format(x_msb, y_msb, z_msb))
    sleep(debounce_time)