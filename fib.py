# Fibanaci sequence at n values
# ITC110
# Jeremy Ward fib.py

# Make main
def main():
    # Fibanaci is a sequence that is 1 + 1 + 2 + 3 etc

    nOne = 1
    nTwo = 1
    nTotal = 0
    #iterate over values till we get to n'th value
    n = int(input('Please Input Nth Value: '))
    for i in range(n-2):
        nTotal = nOne + nTwo
        nOne = nTwo
        nTwo = nTotal
    print(nTotal)

main()
