import math
import pigpio
import time

class Servo:
    def __init__(self, io, pin, maxAngle=180, minAngle=0):
        self.io = io
        self.pin = pin
        self.angle = None
        self.debug = False

        self.maxAngle = maxAngle
        self.minAngle = minAngle
        self.angular_range = maxAngle - minAngle

        self.io.set_mode(self.pin, pigpio.OUTPUT)
        self.io.set_PWM_frequency(self.pin, 50)
        # 1,000,000 / 50 = 20,000us for 100% duty cycle
        self.io.set_PWM_range(self.pin, 20000)
        
        self.io.hardware_PWM(self.pin, 50, 2000)
        self.io.set_PWM_dutycycle(self.pin, 0)
        self.io.set_servo_pulsewidth(self.pin, 0)

    def getValue(self):
        return self.angle;
    
    def angle(self):
        result = self._get_value()
        if result is None:
            return None
        else:
            return round(
                self._angular_range *
                ((result - self._min_value) / self._value_range) +
                self._min_angle, 12)
        
    def setAngle(self, angle):
        if angle is None:
            self.value = None
        elif ((self.min_angle <= angle <= self.max_angle) or
              (self.max_angle <= angle <= self.min_angle)):
            self.value = (
                self._value_range *
                ((angle - self._min_angle) / self._angular_range) +
                self._min_value)
        else:
            raise ValueError(
                f"AngularServo angle must be between {self.min_angle} and "
                f"{self.max_angle}, or None")

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
