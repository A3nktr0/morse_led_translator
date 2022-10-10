"""Function who translate phrase into Morse code."""

from morse_code import MORSE_CODE
import RPi.GPIO as GPIO
import time

ledPin = 11  # Define ledPin


def setup():
    """Initialize GPIO output."""
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, GPIO.LOW)


def translate(user_input):
    """Translate user input into morse code."""
    for character in user_input.upper():
        if character in MORSE_CODE:
            morse_list.append(MORSE_CODE[character]+"_")
        elif character == " ":
            morse_list.append(" ")
    return morse_list


def output_translation(morse_list):
    """Translate into led blink."""
    for letter in morse_list:
        for element in letter:
            if element == ".":
                GPIO.output(ledPin, GPIO.HIGH)
                time.sleep(0.5)
                GPIO.output(ledPin, GPIO.LOW)
                time.sleep(0.5)
            elif element == "-":
                GPIO.output(ledPin, GPIO.HIGH)
                time.sleep(1.5)
                GPIO.output(ledPin, GPIO.LOW)
                time.sleep(0.5)
            elif element == "_":
                GPIO.output(ledPin, GPIO.LOW)
                time.sleep(1.5)
            elif element == " ":
                GPIO.output(ledPin, GPIO.LOW)
                time.sleep(3.5)


def destroy():
    "Interrupt program."
    GPIO.cleanup()


if __name__ == "__main__":
    user_input = input("Enter your phrase: ")
    morse_list = []
    print("MORSE CODE TRANSLATOR\n")
    setup()
    try:
        translate(user_input)
        output_translation(morse_list)
    except KeyboardInterrupt:
        destroy()
