"""
Created by: Julianne Leblanc-Peltier
Created on: Oct 2023
This program generates two random integers between 0 - 99 and displays whether one is greater than the other.
"""

from microbit import *
import random

# variables
first_random_number = random.randint(0, 99)
second_random_number = random.randint(0, 99)

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
        display.scroll(str(first_random_number))
        display.show(Image.HAPPY)

    # if button b is pressed, displays randomly generated second number between 0 - 99.
    if button_b.is_pressed():
        # process
        display.clear()

        # output
        display.scroll("#2:")
        display.scroll(str(second_random_number))
        display.show(Image.HAPPY)

    # if MicroBit was shaken, display which number is greater than the other
    if accelerometer.was_gesture("shake"):
        # process
        display.clear()
        # if first number is greater than second number, display "first number > second number" else, display "first number < second number"
        if first_random_number > second_random_number:
            display.scroll(str(first_random_number))
            display.scroll(">")
            display.scroll(str(second_random_number))
            display.show(Image.SAD)
        else:
            display.scroll(str(first_random_number))
            display.scroll("<")
            display.scroll(str(second_random_number))
            display.show(Image.SAD)
