from adafruit_circuitplayground import cp
import time
def flash_pixels():
    while True:
        cp.pixels.fill((255, 0, 0)) 
        cp.play_tone(500, 0.5) 
        time.sleep(0.5)
        cp.pixels.fill((0, 0, 255)) 
        cp.play_tone(900, 0.5) 
        time.sleep(0.5)
flash_pixels()