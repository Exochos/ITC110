def conversion(isFOrC, passedData):

    if  isFOrC == 1:
        passedData = float((passedData - 32) * 5/9)
        print(passedData)


    elif isFOrC == 2:
        passedData = float((passedData + 32) * 9/5)
        print(passedData)

    else:
        print("Shoudn't get here")


def main():
    while(True):

        print("MENU\n1. Fahrenheift to Celsius: \n2. Celsius to Farhrenheift:\n3 to Quit:  ")
        a = int(input("Enter a Menu Option: "))
        if a == 1:
            b = float(input("Enter Degrees Fahrenheift: "))
            conversion(a,b)
        elif a == 2:
            b = float(input("Enter Degrees Celsius: "))
            conversion(a,b)
        elif a == 3:
            print("Thanks for Coming\n")
            break
        else:
            print("\n\ncouldn't get a valid input Please Try again\n\n")
main()