from gpiozero import LEDBoard
from gpiozero.tools import quantized, random_values
from signal import pause
from time import sleep
from random import randint
def random_values_with_zero():
    while True:
        yield randint(0,10)/10
tree = LEDBoard(*range(2,28),pwm=True)
tree.off()
sleep(1)
tree.pulse()
sleep(1)
for led in tree:
    ## led.source = quantized(random_values(),10)
    led.source = random_values_with_zero()
    print(led.value)
    led.source_delay = 0.75
pause()