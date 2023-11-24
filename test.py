from time import sleep
from adafruit_servokit import ServoKit

kit = ServoKit(channels=8)
while True:
    kit.servo[0].angle = 0
    sleep(1)
    kit.servo[1].angle = 0
    sleep(1)
    kit.servo[2].angle = 0
    sleep(1)
    kit.servo[0].angle = 45
    sleep(1)
    kit.servo[1].angle = 45
    sleep(1)
    kit.servo[2].angle = 120
    sleep(1)
