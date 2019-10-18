from gpiozero import *
from time import sleep

b = Button(15) # Button at GPIO15
ld = LED(14) # Led at GPIO14

while True:
    if b.is_pressed:
        ld.toggle()
        sleep(1) # Attend 1 seconds