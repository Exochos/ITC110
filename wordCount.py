# wordCount.py
# This program counts the number of words in an input stream
# Jeremy Ward --- ITC110


def main():
       userInput = input("Please enter an input string: ")     #Read from input
       a = userInput.split()                                   #Split Input
       print(len(a))                                           #Print how many words we found
main()