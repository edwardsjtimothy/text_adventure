#importing creature constructor function
import random
from creatures.adventurers import Wizard, Rogue, Barbarian
from miscellaneous.misc import errHandle

isWiz = False
isRog = False
isBar = False

#main menu function
def main():
    print("                                                                       ************What is your name, traveller?************")
    global name
    name = input()
    print("Hello, " + name)
    print("                                                                             ************Choose your Class************")
    
    def charChoice():
        choice = input("""
            A: Wizard
            B: Rogue
            C: Barbarian
                """) 
        # a builds a wizard object
        if choice == "A" or choice =="a":
            print("""
                You have selected Wizard!
                Here are you starting stats.
            """)
            global wizard
            wizard = Wizard(name, 10, 50)
            print(f"""
                ||Name: {wizard.name}     ||
                ||Health: {wizard.health} ||
                ||Mana: {wizard.mana}     ||
            """)
            global isWiz
            isWiz = True
        # b builds a rogue object 
        elif choice == "B" or choice =="b":
            print("""
                You have selected Rogue!
                Here are you starting stats.
            """)
            global rogue
            rogue = Rogue(name, 15, 100)
            print(f"""
                ||Name: {rogue.name}     ||
                ||Health: {rogue.health} ||
                ||Focus: {rogue.focus}   ||
            """)
            global isRog
            isRog = True
        # c builds a barbarian object 
        elif choice == "C" or choice =="c":             
            print("""
                You have selected Barbarian!
                Here are you starting stats.
            """)
            global barbarian
            barbarian = Barbarian(name, 20, 100)
            print(f"""
                ||Name: {barbarian.name}     ||
                ||Health: {barbarian.health} ||
                ||Max Rage: {barbarian.rage} ||
            """)
            global isBar
            isBar = True
        else:
            errHandle(charChoice)
    charChoice()

    # function to determine likelihood of random combat encounter
def ambush():
    if isWiz:
        print("Wizard")
    elif isRog:
        print("Rogue")
    elif isBar:
        print("Barbarian")


    # amAmbushed = random.randrange(1,21)













    
        

