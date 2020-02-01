







def main():


    print("Change Counter\n\n")


    quarterS    = int(input("Please input the number of quarters: "))
    dimeS       = int(input("Please input the number of dimes: "))
    nickleS     = int(input("Please input the number of nickles "))
    pennieS     = int(input("Please input the number of pennies: "))


    total = float(quarterS * .25 + dimeS * .10 + nickleS * .05 + pennieS * .01)

    print("Your total is ", total)


main()