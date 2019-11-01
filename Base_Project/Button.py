from gpiozero import Button, LED
from time import sleep
from logger import log

b = Button(15) # Button at GPIO15
ld = LED(14) # Led at GPIO14

while True:
    if b.is_pressed:
        ld.toggle()
        log("Button pressed")
        sleep(1) # Wait 1 second
