#---Code Start Here---
from gpiozero import LED
from time import sleep

#---Led Blink---
led = LED(14) # Led connected at GPIO14

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
