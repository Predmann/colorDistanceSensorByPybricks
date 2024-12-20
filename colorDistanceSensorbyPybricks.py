from pybricks.pupdevices import ColorDistanceSensor, DCMotor # ColorSensor instead of ColorDistanceSensor if using Mindstorms sensor
from pybricks.parameters import Color, Port 
from pybricks.tools import wait

motor = DCMotor(Port.A) # Motor connected to port A
sensor = ColorDistanceSensor(Port.B) # ColorSensor instead of ColorDistanceSensor if using Mindstorms sensor

# Constants
LIGHT = 57
DARK = 16
station_stop_time_ms = 5000
eol_stop_time_ms = 1500
forward_speed = 50
check_color_interval_ms = 20

# Function to check for a specific color
def check_for_color(color):
    while sensor.color() != color:
        wait(check_color_interval_ms)

# Main loop
while True:

    # Sensor checks for green, will do a pause and move forward
    print("...looking for green...")
    check_for_color(Color.GREEN)
    Kolor = str(sensor.color())
    print(Kolor+" detected, at station, stopping and continuing...")
    motor.brake()
    for i in range(1000, 10000):
    wait(i)
    motor.dc(forward_speed)

    # Sensor checks for blue, will do a pause and move back
    print("...looking for blue...")
    check_for_color(Color.BLUE)
    Kolor = str(sensor.color())
    print(Kolor+" detected, at end of line, stopping and going back to station...")
    motor.brake()
    for j in range(1000, 10000):
    wait(j)
    motor.dc(forward_speed)
