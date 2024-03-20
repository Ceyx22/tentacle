import servoController
import time

def test():
    servo = servoController.Controller()
    servo.setAccel(0,25)
    servo.setTarget(0,6000)
    servo.setAccel(1,25)
    servo.setTarget(1,6000)
    time.sleep(2)
    servo.setAccel(0,25)
    servo.setTarget(0,1000)
    servo.setAccel(1,25)
    servo.setAccel(1,1000)
    servo.close

def sub():
    servo = servoController.Controller()
    servo.runScriptSub(0)
    print("sub0")
    time.sleep(3)
    servo.runScriptSub(1)
    print("sub1")

if __name__ == "__main__":
    test()
    