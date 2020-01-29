## File chaos.py
## a simple program to illustrate chaotic behavior in computers

def main():
    print("This Program illustrates a chaotic function")
    x = eval(input("Please enter a number between 0 and 1: "))

    y = x
    z = x

    n = eval(input("Please enter the number of iterations: "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        y = 3.9 * (x -x * x)
        z = 3.9 * x - 3.9 * x * x
        print(x, "\n", y, "\n", z, "\n")
main()
