from pybricks.pupdevices import ColorDistanceSensor, DCMotor
from pybricks.parameters import Color, Port
from pybricks.tools import wait

motor = DCMotor(Port.A)  # Motor connected to port A
sensor = ColorDistanceSensor(Port.B)  # Sensor connected to port B

# Constants
station_stop_time_ms = 10000  # stop at station for 10 seconds
forward_speed = 50            # normal speed
slow_speed = 20               # reduced speed
check_color_interval_ms = 50  # how often to check (ms)

last_color = None  # store previously detected color

while True:
    kolor = sensor.color()

    if kolor != last_color:  # react only to a change in color
        last_color = kolor

        if kolor == Color.GREEN:
            print("Green detected → driving forward.")
            motor.dc(forward_speed)

        elif kolor == Color.RED:
            print("Red detected → stopping for 10 seconds.")
            motor.brake()
            wait(station_stop_time_ms)
            print("Resuming forward movement...")
            motor.dc(forward_speed)

        elif kolor == Color.BLUE:
            print("Blue detected → slowing down.")
            motor.dc(slow_speed)

        else:
            print("No special color → continuing current action.")

    wait(check_color_interval_ms)
