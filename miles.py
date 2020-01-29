## File: miles.py
## Takes a user input in the form of kilometers
## outputs input as miles

def main():

    print("This program converts kilometers to miles.")
    kiloM = eval(input("Please enter your input value in kilometers "))
    miles = 0.62 * kiloM

    print("The distance in miles is: ", miles)

main()
