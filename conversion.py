## File: conversion.py
## Takes a user input to ask

def main():

    print("This program converts Centigrade to Fahrenheit.")
    c = eval(input("Please enter your input value in kilometers "))
    f = 0.621371 * c + 32

    print("The fahrenheit temperature is: ", f)

main()
