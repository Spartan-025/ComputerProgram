from adafruit_circuitplayground import cp
import time
def update_leds(num_pixels):
    for i in range(10):
        if i < num_pixels:
            cp.pixels[i] = (0, 255, 0)  
        else:
            cp.pixels[i] = (0, 0, 0)  
def calculate_lit_pixels(brightness):
    if brightness <= 3:
        return 10
    elif brightness <= 6:
        return 9
    elif brightness <= 9:
        return 8
    elif brightness <= 12:
        return 7
    elif brightness <= 15:
        return 6
    elif brightness <= 18:
        return 5
    elif brightness <= 21:
        return 4
    elif brightness <= 24:
        return 3
    elif brightness <= 27:
        return 2
    elif brightness <= 30:
        return 1
    else:
        return 0  
while True:
    brightness = cp.light 
    num_pixels = calculate_lit_pixels(brightness)
    update_leds(num_pixels)
    print(f"Brightness: {brightness}, Lit Pixels: {num_pixels}")
    time.sleep(0.5)