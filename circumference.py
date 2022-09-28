#!/usr/bin/env python3

# Created by: Marshall Demars
# Created on: Sept 2022
# This program calculates circumference of a circle
#    with user input

import math
import constants


def main():
    # this function calculates the area and perimeter

    # input
    radius_of_circle = int(input("Enter radius of the circle (mm): "))

    # process
    circumference = constants.TAU * radius_of_circle

    # output
    print("\nCircumference is {} mm.".format(circumference))

    print("\nDone.")


if __name__ == "__main__":
    main()
