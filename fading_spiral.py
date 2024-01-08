from machine import Pin
from neopixel import NeoPixel
from time import sleep_ms
# effect by https://github.com/vladultimate 
pixels = NeoPixel(Pin(16), 25)

pixel = [0, 1, 2, 3, 4, 9, 14, 19, 24, 23, 22, 21, 20, 15, 10, 5, 6, 7, 8, 13, 18, 17, 16, 11, 12]

end_pixel = [12, 11, 16]

def clear(neopixels):
    neopixels.fill((0, 0, 0))
    neopixels.write()

def fading_spiral():
    for index, value in enumerate(pixel):

        pixels[value] = (3, 3, 5)
        if index > 0:
            pixels[pixel[index - 1]] = (2, 2, 4)
        if index > 1:
            pixels[pixel[index - 2]] = (1, 1, 3)
        if index > 2:
            pixels[pixel[index - 3]] = (0, 0, 0)
        pixels.write()
        sleep_ms(75)

    for index in range(2, -1, -1):  # Идем в обратном порядке
        pixels[end_pixel[index]] = (0, 0, 0)
        pixels.write()
        sleep_ms(75)

while True:
    fading_spiral()
    clear(pixels)
    sleep_ms(600)
