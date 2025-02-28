#!/usr/bin/env python3

# Created By: Amara Tie 

# Date: Month Februray 28, 2025

# Calculating the circumferance using tau
import constants 


def main():
    # Get Radius 
    radius = float(input("Enter the radius of the circle (mn): "))

    # Calculate the circumference
    circumference = constants.TAU* radius 

    # Display the circumferance
    print("")
    print("Circumference = {} mn".format(circumference))


if __name__=="__main__":
     main()