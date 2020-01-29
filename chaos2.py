## File chaos.py
## a simple program to illustrate chaotic behavior in computers

def main():


    x, y = eval(input("enter a number between 0 and 1: ")), eval(input(" enter a second number between 0 and 1: "))


    n = eval(input("Please enter the number of iterations: "))

    print("Input \t\t", x, "\t\t\t", y, "\n")
    for i in range(n):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print("\t\t", x, "\t", y)
main()
