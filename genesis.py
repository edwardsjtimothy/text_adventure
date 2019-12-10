#importing creature constructor function
from adventurers import Wizard

#character name function 

def name():
    print("************What is your name, traveller?***********")
    global name
    name = input()
    print("Hello, " + name)

#main menu function
def main():
    name()
    print("**********Choose your Class**********")
    choice = input("""
        A: Wizard
        B: Rogue
        C: Barbarian
              """)
    if choice == "A" or choice =="a":
        print("You have selected Wizard!")
        char = Wizard(name, 10, 20)
        stats = """
            ||Name: {} ||
            ||Health: {} ||
            ||Mana: {} ||
        """
        print(stats.format(char.name, char.health, char.mana))
    elif choice == "B" or choice =="b":
        print("You have selected Rogue!")
    elif choice == "C" or choice =="c":             
        print("You have selected Barbarian!")





main()