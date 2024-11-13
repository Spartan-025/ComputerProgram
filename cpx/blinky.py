from adafruit_circuitplayground import cp
import time
def flash():
    while True:
        cp.pixels.fill((0, 255, 0))
        time.sleep(0.367) 
        cp.pixels.fill((0, 255, 0))