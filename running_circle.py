from time import sleep_ms
from machine import Pin
from neopixel import NeoPixel

pixels = NeoPixel(Pin(16), 25)

def clear(neopixels):
    neopixels.fill((0, 0, 0))
    neopixels.write()


def write_symbol(neopixels, symbol, color):
    for ax in symbol:
        neopixels[ax[0]*5+ax[1]] = (color[1], color[0], color[2])
    neopixels.write()


colors = [(0, 0, 5), (0, 5, 5), (0, 5, 0), (5, 5, 0), (5, 0, 0), (5, 0, 5)]
while True:
    for color in colors:
        for i in range(1, 5):
            axes1 = [(0, i), (i, 4), (4, 4-i), (4-i, 0)]
            axes2 = [((i%3)+1, 1), (3, (i%3)+1), (3-(i%3), 3), (1, 3-(i%3))]
            axes = axes1 + axes2
            for ax in axes:    
                pixels[ax[0]*5+ax[1]] = (color[1], color[0], color[2])
        

            pixels.write()
        
            sleep_ms(75)
        
            clear(pixels)