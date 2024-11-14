from adafruit_circuitplayground import cp
def random_color():
    import random
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

while True:
    x, y, z = cp.acceleration
    print("X:", x, "Y:", y, "Z:", z)
    threshold = 18.0
    cp.pixels.brightness = 0.2

    if abs(x) > threshold or abs(y) > threshold or abs(z) > threshold:
        print("Shaking detected!")
        
        for i in range(10):
            cp.pixels[i] = random_color()