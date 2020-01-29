# calculate 3 test scores average


#print("Enter n number of  test scores")
def main():

    # get scores from the user
    totalScore = 0       # initialize variable


    n = eval(input("Please enter what number of test scores you would like to input: "))

    for i in range(n):
        totalScore += eval(input("Please enter a test score: "))

    # calculate average score
    averageScore = round(totalScore / n)

    # display the result
    print("Total Score:  ", totalScore, "\nAverage Score:", averageScore)

main()