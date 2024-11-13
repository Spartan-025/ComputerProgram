from adafruit_circuitplayground import cp

import time
while True:
    if cp.button_a:
        cp.pixels.brightness = 0.2
        for i in range(10):
            cp.pixels[i] = (0, 0, 225)  
            time.sleep(0.1) 
            cp.pixels[i] = (0, 0, 0) 
            time.sleep(0.1)
        while cp.button_a: 
            pass
    else:
        cp.pixels.fill((0,0,0))

        