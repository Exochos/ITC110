## This is a program which computes the cost of a pizza by the 360* inch

#   import math library
import math as m


def main():

    print("This program computes the cost per square inch of a pizza.\n\n")

    # get the diameter and convert to radius
    radius = (float(input("Enter the diameter of the pizza (in inches): "))/2)

    #get the price in cents
    price = float(input("Enter the price of the pizza in cents: "))

    # area is equal to radius^2 * pi
    area = m.pi * (radius ** 2)

    # price / area and then round the value to 2 decimal points
    finalValue = round((price / area),2)

    print(finalValue)

main()
