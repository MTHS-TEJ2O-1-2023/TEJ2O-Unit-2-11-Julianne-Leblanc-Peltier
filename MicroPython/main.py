"""
Created by: Julianne Leblanc-Peltier
Created on: Oct 2023
This program generates two random integers between 0 - 99 and displays whether one is greater than the other.
"""

from microbit import *
from random import *

# variables
first_random_number = random.randrange(0, 99)
second_random_number = random.randrange(0, 99)

# cleanup
display.clear()
display.show(Image.HAPPY)

while True:
    # if button a is pressed, displays randomly generated first number between 0 - 99.
    if button_a.is_pressed():
        # process
        display.clear()

        # output
        display.scroll("#1:")
        display.schow(str(first_random_number))
        display.show(Image.HAPPY)

    # if button b is pressed, displays randomly generated second number between 0 - 99.
    if button_b.is_pressed():
        # process
        display.clear()

        # output
        display.scroll("#2:")
        display.show(str(second_random_number))
        display.show(Image.HAPPY)
    if accelerometer.was_gesture("shake"):
        # process
        display.clear()

        if first_random_number > second_random_number():
            display.show(str(first_random_number))
            display.scroll(">")
            display.show(str(second_random_number))
            display.show(Image.SAD)

        else:
            display.show(str(first_random_number))
            display.scroll("<")
            display.show(str(second_random_number))
            display.show(Image.SAD)
