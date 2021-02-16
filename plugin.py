#BMO055 plugin for SignalK https://github.com/munnecke/sk-plugin-BMO055

import sys, json, threading, time;
import board, busio, adafruit_bno055; #these import modules are from Adafruit

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055_I2C(i2c)
last_val = 0xFFFF
n = 0
def outputSk():  # retreive data from the sensor and put into JSON forma
    global n
    temp = ' {"path": "environment.temperature","value": ' + str(sensor.temperature) + ' },'
    bearing = ' {"path": "environment.compass","value": ' + str(sensor.euler[0]) + ' },'
    heel = ' {"path": "environment.heel","value": ' + str(sensor.euler[1]) + ' },'
    pitch = ' {"path": "environment.pitch","value": ' + str(sensor.euler[2]) + ' }' #note no trailing comma on last one
    skData = '{"updates":[{"values":[' + temp + bearing + heel + pitch + ']}]}'

    
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
