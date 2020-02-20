# factorial.py
#    Program to compute the factorial of a number
#    Illustrates for loop with an accumulator

def main():

    n = int(input("Please enter a whole number: "))     #input
    z = n                                               #temp variable

    temp = n                                            #more temp variables

    for i in range(1,n,):                               #from 1 to n

        n -= 1                                          #decrement loop
        temp = temp * n                                 #initial 


    print("The Factorial of ", + z, "is ", + temp)


main()