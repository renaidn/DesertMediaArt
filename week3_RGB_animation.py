#Name: Adina Maratkyzy
#Class: Desert Media Art
#RGB animation sequence
#Title: a whole lifespan

import time
import board
import random

if hasattr(board, "APA102_SCK"):
    import adafruit_dotstar

    led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
else:
    import neopixel

    led = neopixel.NeoPixel(board.NEOPIXEL, 1)

#a sequence that imitates heartbeat through blinking and change in led brightness
def heartbeat_animation(direction, duration, color):
    interval = 0.2 #time LED is on
    steps = int(duration / interval) #number of for loop iterations
    if direction == 1: #identify if it's the first heartbeat sequence
        for i in range(steps/2):
            led.brightness = (i/100) #for the brightness to increase over time
            led[0] = (255, 255, 0) #yellow color
            time.sleep(interval)
            led[0] = (0, 0, 0) #black color
            time.sleep(0.7) #time LED is off
    elif direction == 2: #identify if it's the second heartbeat sequence
        for i in range(steps):
            led.brightness = (0.2)
            print(led.brightness)
            led[0] = (255, 255, 0)
            time.sleep(interval)
            led[0] = (0, 0, 0)
            time.sleep(0.9) #increased black led display to imitate slower heartbeat

#random color generator
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

#a sequence of random colors played at varied speed
def random_animation(duration):
    led.brightness = 1
    start_time = time.monotonic() #record current time as a reference point
    peak_time = 15.0  # change speed at 15 seconds
    #make sure that the loop goes on for 25 seconds
    while time.monotonic() - start_time < duration: 
        elapsed_time = time.monotonic() - start_time #calculate time passed
        #accelerate towards 15 seconds mark, gradually slow down after that
        if elapsed_time < peak_time:
            blink_interval = 1.0 / (elapsed_time + 1)  # speed up
        else:
            blink_interval = 1.0 / (duration - elapsed_time + 1)  # slow down
        led[0] = random_color() #choose a random color
        time.sleep(blink_interval) 

#combine into a big sequence
def main_animation():
    # first heartbeat sequence
    heartbeat_animation(1, 5, (255, 255, 0))

    # random color sequence with variable speed
    random_animation(25)

    # final heartbeat sequence
    heartbeat_animation(2, 5, (255, 255, 0))

    # turn off LED for 5 seconds for dramatic effect
    led[0] = (0, 0, 0)
    time.sleep(5)

while True:
    main_animation() #play main animation sequence

