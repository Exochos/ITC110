# Fibanaci sequence at n values
# ITC110
# Jeremy Ward WindChill.py
import math
import cmath


# Honestly this whole program is coddled together out of hopes
# and prayers

#this is where we calculate the tempatures
def formula(temp,wind_chill):
    a = 35.74 + 0.6215*temp
    b = 35.75 * (math.pow(wind_chill,.16))
    c = 0.4275*temp*(math.pow(wind_chill,0.16))
    return(round(a - b + c))

# Make main
def main():

    #This bit here prints the outside of the table
    print('-----+--------------------------------------------------')
    print(" MPH  |   ", end='')
    for i in range(-20,70,10):
        print(str(i) + '   ', end='')
    print('\n-----+--------------------------------------------------')


    # This prints the actual guts of the table
    for i in range(0,51,5):
        # This prints the first values cause wind_chill does work < 3MPH
        if (i < 5):
            print('   ', + i, '|   ',  end='')
            for i in range(-20,70,10):
                print(str(i) + '   ', end='')
            print('')
        #this is here cause I was getting some wierd off by one bugs
        elif (i==5):
            print('   ', + i, '| ',  end='')
            for z in range(-20,70,10 ):
                print(' ',str(formula(z,i)).rjust(3), end='')
            print('')
        #This prints most of the actual guts of the program
        else:
            print('  ', + i, '| ',  end='')
            for z in range(-20,70,10 ):
                    print(' ',str(formula(z,i)).rjust(3), end='')
            print('')

    #Printing the outside of the program
    print('-----+--------------------------------------------------')
main()
