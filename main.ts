/* Copyright (c) 2023 MTHS All rights reserved
 *
 * Created by: Julianne Leblanc-Peltier
 * Created on: Oct 2023
 * This program generates two random integers between 0 - 99 and displays whether one is greater than the other.
*/

let firstRandomNumber: number = 0
let secondRandomNumber: number = 0

basic.clearScreen()
basic.showIcon(IconNames.Happy)

// if button a is pressed, displays randomly generated first number between 0 - 99.
input.onButtonPressed(Button.A, function () {
  // process
  firstRandomNumber = randint(0, 99)
  basic.clearScreen()
  // output
  basic.showString('#1:')
  basic.showNumber(firstRandomNumber)
  basic.showIcon(IconNames.Happy)
})

// if button b is pressed, displays randomly generated second number between 0 - 99.
input.onButtonPressed(Button.B, function () {
  // process
  secondRandomNumber = randint(0, 99)
  basic.clearScreen()

  // output
  basic.showString('#2:')
  basic.showNumber(secondRandomNumber)
  basic.showIcon(IconNames.Happy)
})

// if MicroBit shaken, displays whether the first number is greater or lesser than second number
input.onGesture(Gesture.Shake, function () {
  basic.clearScreen()
  // displays first number is greater than second number
  if (firstRandomNumber > secondRandomNumber) {
    basic.showNumber(firstRandomNumber)
    basic.showString('>')
    basic.showNumber(secondRandomNumber)
    basic.showIcon(IconNames.Sad)
  } else {
    // displays first number is lesser than second number
    basic.showNumber(firstRandomNumber)
    basic.showString('<')
    basic.showNumber(secondRandomNumber)
    basic.showIcon(IconNames.Sad)
  }
})
