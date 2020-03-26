6#cLASSES.PY
# Jeremy Ward ITC 110
# Makes a pretty basic sharky which can do various things

# This is the class instantiator
class Shark:
    def __init__(self, name, people_eaten):
        self.name = name
        self.noms = people_eaten

    # One of two varius actions shark can do
    def swim(self):
        # swim
        print(self.name + " is swimming.\n")

    # Shark is hungry
    def nom(self):
        # nom
        self.noms += 1
        print(self.name + " Has nommed: ", self.noms, "people\n")


def main():
    # Set name of Shark object
    name = input("Please enter the name of your shark: ")
    noms = int(input("How many people has your shark eaten: "))
    baby_shark = Shark(name, noms)

    #Loop while the user is deciding.
    while(True):
        a = int(input("Please enter a command\n 1 to swim \n 2 to Eat a person\n 3 to quit\n:"))
        if (a==1):
            baby_shark.swim()
        elif(a==2):
            baby_shark.nom()
        elif(a==3):
            break

main()