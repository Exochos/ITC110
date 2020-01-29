# futval.py
#    A program to compute the value of an investment
#    carried 10 years into the future

def main():
    print("This program calculates the future value, given an initial investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    time = eval(input("Enter the number of years: "))

    for i in range(time):
        principal = principal * (1 + apr)

    print ("The value in ", time, "Number of years is: ", round(principal))

main()
