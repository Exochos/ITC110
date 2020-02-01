# mario.py
# this program creates
def main():
    y = input("Please enter the size of the pyramid you would like:  ")
    y = int(y)
    x = 0

    for i in range(y):
        for x in range(y):
            print(" ", end = "")
        

##        print(" " * (y-1-i), end="")
##      print("#" * (i+2), end="")
##      print(" ")

main()
