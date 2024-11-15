from adafruit_circuitplayground import cp
import time
NUM_PIXELS = 10
lit_pixels = 0 
cp.pixels.brightness = 0.2
def lights():
    for i in range(NUM_PIXELS):
        if i < lit_pixels:
            cp.pixels[i] = (0, 255, 0) 
        else:
            cp.pixels[i] = (0, 0, 0)
while True:
    if cp.button_a: 
        if lit_pixels < NUM_PIXELS:
            lit_pixels += 1
            lights()
            time.sleep(0.2)
    if cp.button_b: 
        if lit_pixels > 0:
            lit_pixels -= 1
            lights()
            time.sleep(0.2)

    time.sleep(0.1)