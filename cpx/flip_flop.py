from adafruit_circuitplayground import cp
import time

while True:
    if cp.switch: 
        cp.pixels.brightness = 0.2
        cp.pixels[0:5] = [(0, 255, 0)] * 5 
        cp.pixels[5:10] = [(0, 0, 0)] * 5  
    else:  
        cp.pixels.brightness = 0.2
        cp.pixels[0:5] = [(0, 0, 0)] * 5  
        cp.pixels[5:10] = [(0, 255, 0)] * 5 
    
    time.sleep(0.5)