#Name: Adina Maratkyzy
#Class: Desert Media Art
#photoresistor and led
#Title: Possessed House

import board
import neopixel
import time
import analogio

# Define the number of pixels and create a NeoPixel object
NUM_PIXELS = 1
pixels = neopixel.NeoPixel(board.NEOPIXEL, NUM_PIXELS)

# Define the colors (orange, red, green, and purple)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)

# Define the number of steps for the transition
NUM_STEPS = 100

# Initialize the photoresistor on analog input A0
photoresistor = analogio.AnalogIn(board.A0)

# Function to interpolate between two colors
def interpolate_color(color1, color2, factor):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    r = int(r1 + (r2 - r1) * factor)
    g = int(g1 + (g2 - g1) * factor)
    b = int(b1 + (b2 - b1) * factor)
    return (r, g, b)

# Main animation loop
while True:
    # Read the photoresistor value
    photoresistor_value = photoresistor.value

    # Check if the photoresistor value is in the desired range
    if 0 <= photoresistor_value <= 800:
        for step in range(NUM_STEPS + 1):
            # Calculate the interpolation factor
            factor = step / NUM_STEPS
            # Interpolate between ORANGE and RED
            color = interpolate_color(ORANGE, RED, factor)
            # Set the RGB LED color
            pixels.fill(color)
            pixels.show()
            # Delay to control the animation speed
            time.sleep(0.05)  # Adjust the sleep duration as needed
        # Transition from RED to ORANGE
        for step in range(NUM_STEPS + 1):
            factor = step / NUM_STEPS
            color = interpolate_color(RED, ORANGE, factor)
            pixels.fill(color)
            pixels.show()
            time.sleep(0.05)
    else:
        # If the photoresistor value is outside the desired range, turn off the LED
        pixels.fill((0, 0, 0))
        pixels.show()
