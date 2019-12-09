#importing creature constructor function
from adventurers import *

#main menu function
def main():
    print("**********Choose your Class**********")
    choice = input("""
        A: Wizard
        B: Rogue
        C: Barbarian
              """)
    if choice == "A" or choice =="a":
        print("You have selected Wizard!")
    elif choice == "B" or choice =="b":
        print("You have selected Rogue!")
    elif choice == "C" or choice =="c":             
        print("You have selected Barbarian!")


main()