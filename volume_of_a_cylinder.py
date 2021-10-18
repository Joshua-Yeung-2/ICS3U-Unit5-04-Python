# !/usr/bin/env python3

# Created by Joshua Yeung
# Created on October 2021
# This program is to calculates the volume of a cylinder

import math


def volume_of_cylinder(radius, height):
    # This function is to calculates the volume of a cylinder

    # process
    volume = math.pi * radius ** 2 * height
    return volume


def main():
    # this function gets the radius and the height

    # input
    radius = input("Enter the radius (mm): ")
    height = input("Enter the height (mm): ")
    print("")

    # process
    try:
        radius_int = int(radius)
        height_int = int(height)

        # call functions
        volume_of_cylinder_2 = volume_of_cylinder(radius = radius_int, height = height_int)
        print("The volume of the cylinder is {} mm³".format(volume_of_cylinder_2))

    except Exception:
        print("sorry, this is not a number")
        print("please try again")

    print("\nDone")


if __name__ == "__main__":
    main()
