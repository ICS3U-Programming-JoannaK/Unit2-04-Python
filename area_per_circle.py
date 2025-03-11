#!/usr/bin/env python3


# Created by: Joanna Keza
# Date: March 10, 2025
# This program calculates the area and
# circumference of a circle using PI

import math


def main():
    # get the radius from the user
    radius = float(input("Enter the radius of the circle (mm): "))

    # calculate the circumference and area
    circumference = 2 * math.pi * radius
    area = math.pi * radius**2

    # display the circumference and area
    print("")
    print("Circumference = {:,.2f} mm".format(circumference))
    print("Area = {:,.2f} mm".format(area))


if __name__ == "__main__":
    main()