# sk-plugin-BMO055

This is a signal K plugin for the BMO055 IMU. https://www.adafruit.com/product/2472

My primary goal is to learn how SignalK plugins work, so I am modifying https://github.com/SignalK/sk-plugin-python-demo

## Development

- clone the plugin from Github
- `npm link` in the plugin directory
- `npm link sk-plugin-python-demo` in your server directory

##Goals
I plan to read the acceleration from the sensor and derive higher level deriviatives of acceleration.  from Newton's laws:  
change in position over time is velocity, change in velocity is acceleration (raw data from the sensor).  The plugin will also compute
change in accleration over time (jerk), change in jerk (snap), change in snap (crackle), and change in crackle (pop).  Full API for the sensor
is at https://circuitpython.readthedocs.io/projects/bno055/en/latest/api.html


