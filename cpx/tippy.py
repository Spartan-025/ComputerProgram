from adafruit_circuitplayground import cp

while True:
    x, y, z = cp.acceleration
    print("X:", x, "Y:", y, "Z:", z)
    if x > 5:
        print("Tilted right")
        cp.pixels.brightness = 0.2
        cp.pixels[1] = (0, 255, 0)
        cp.pixels[2] = (0, 255, 0)
        cp.pixels[3] = (0, 255, 0)
        cp.pixels[6] = (0, 0, 0)
        cp.pixels[7] = (0, 0, 0)
        cp.pixels[8] = (0, 0, 0)

       
    elif x < -5:
        print("Tilted left")
        cp.pixels.brightness = 0.2
        cp.pixels[6] = (0, 255, 0)
        cp.pixels[7] = (0, 255, 0)
        cp.pixels[8] = (0, 255, 0)
        cp.pixels[1] = (0, 0, 0)
        cp.pixels[2] = (0, 0, 0)
        cp.pixels[3] = (0, 0, 0)
    else:
        print("Not tilted")
        cp.pixels.brightness = 0.2
        for i in range(10):
            cp.pixels[i] = (0, 0, 0)
    if y > 5:
        print("Tilted forward")
    elif y < -5:
        print("Tilted backward")