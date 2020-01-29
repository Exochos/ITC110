def main():
    y = input("Please enter the correct size:  ")
    y = int(y)

    for i in range(y):
        print(" " * (y-1-i), end="")
        print("#" * (i+2), end="")
        print(" ")

main()
