from adafruit_circuitplayground import cp
import random
import time
pixel_color = (0, 255, 225) 
while True:
    if cp.button_a:
        print("Button A pressed")
        random_pixel = random.randint(0, 9)
        cp.pixels.fill((0, 0, 0))
        cp.pixels.brightness = 0.2
        cp.pixels[random_pixel] = pixel_color
        time.sleep(0.5)
    if cp.button_b:
        print("Button B pressed")
        cp.pixels.fill((0, 0, 0))
        time.sleep(0.5)