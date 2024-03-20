import math
import pigpio

class Servo:
    def __init__(self, io, pin):
        self.io = io
        self.pin = pin
        self.angle = 0
        self.bebug = False

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
        self.setAngle(0):


if __name__ == "__main__":
    import pigpio
    io = pigpio.pi()
    servo1 = Servo(io)