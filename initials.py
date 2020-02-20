# initials.py
# a program to print out the initials of a given name
# by Jeremy Ward --- ITC110

def main():

       userInput = input("Please enter an input string: ")  ## Get input
       initials = userInput[0]                              ## First letter of input should (hopefully) also always be the first letter
       for a in range(len(userInput)):                      ## Now we loop for lenght of userinput
           if userInput[a].isspace() == True:               ## if we find a space we can (again hopefully) assume the next char will be the value we want
               initials += userInput[a+1]                   ## here we add all the values together

       print(initials.upper())                              ## and finally we output the results to the user

main()