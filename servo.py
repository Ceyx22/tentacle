import math
import pigpio
import time

class Servo:
    def __init__(self, io, pin):
        self.io = io
        self.pin = pin
        self.angle = 0
        self.debug = False

        self.io.set_mode(self.pin, pigpio.OUTPUT)
        self.io.set_PWM_range(self.pin, 255)
        self.io.set_PWM_frequency(self.pin, 1000)
        self.io.set_PWM_dutycycle(self.pin, 0)

    def setAngle(self, angle):
        sig = angle/ 18 + 2
        if self.debug:
            print(f"Angle: {angle}, sig: {sig}")
        self.io.set_PWM_dutycycle(self.pin, sig)


    def powerOff(self):
        if self.debug:
            print("Powering off")
        self.setAngle(0)


if __name__ == "__main__":
    import pigpio
    import time
    import sys
    io = pigpio.pi()
    servo1 = Servo(io, 19)
    if not io.connected:
        print("unable to connect")    
    while True:
        for i in range(360):
            servo1.setAngle(i)
            print(i)
            time.sleep(0.1)
