import sys, json, threading, time;

import board, busio, adafruit_bno055; #these import modules are from Adafruit
 
# Use these lines for I2C
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)
last_val = 0xFFFF
 
while True:
    print("Temperature: {} degrees C".format(sensor.temperature))
    print("Accelerometer (m/s^2): {}".format(sensor.acceleration))
    print("Magnetometer (microteslas): {}".format(sensor.magnetic))
    print("Gyroscope (rad/sec): {}".format(sensor.gyro))
    print("Euler angle: {}".format(sensor.euler))
    print("Quaternion: {}".format(sensor.quaternion))
    print("Linear acceleration (m/s^2): {}".format(sensor.linear_acceleration))
    print("Gravity (m/s^2): {}".format(sensor.gravity))
    print()
 
    time.sleep(3)

n = 0
def outputSk():
    global n
    skData = {'updates': [{ 'values': [{'path': 'some.path', 'value': n}]}]}
    sys.stdout.write(json.dumps(skData) + '\n' + json.dumps(skData))
    sys.stdout.write('\n')
    sys.stdout.flush()
    n += 1
    threading.Timer(1.0, outputSk).start()

threading.Timer(1.0, outputSk).start()

for line in iter(sys.stdin.readline, b''):
    try:
        data = json.loads(line)
        sys.stderr.write(json.dumps(data))
    except:
        sys.stderr.write('error parsing json\n')
        sys.stderr.write(line)

