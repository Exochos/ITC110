# mario.py
# Jeremy Ward
# Make it so
def spaces(x):
    for i in range(x):
        print(" ", end="")

def hashes(x):
    for i in range(x):
        print("#", end="")

def main():

    height = int(input("Please Enter a height of your pyramid: "))
    for i in range(height +1):
        spaces(height)
        hashes(i)
        print("")
        height = height - 1

main()