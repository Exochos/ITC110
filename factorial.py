# factorial.py
#    Program to compute the factorial of a number
#    Illustrates for loop with an accumulator

def main():

    n = int(input("Please enter a whole number: "))
    z = n

    temp = n

    for i in range(1,n,):

        n -= 1
        temp = temp * n


    print("The Factorial of ", + z, "is ", + temp)


main()