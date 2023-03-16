import time
from machine import Pin, PWM
MIN_DUTY = 1000
MAX_DUTY = 10000
pwm = PWM(Pin(0))
pwm.freq(50)
duty = MIN_DUTY
direction = 1
while True:
    for _ in range(1024):
        duty += direction
        if duty > MAX_DUTY:
            duty = MAX_DUTY
            direction = -direction
        elif dut < MIN_DUTY:
            duty = MIN_DUTY
            direction = -direction
        pwm.duty_u16(duty)
