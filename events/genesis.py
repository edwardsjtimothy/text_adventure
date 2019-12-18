#importing creature constructor function
import random
from creatures.adventurers import Wizard, Rogue, Barbarian


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
        else:
            print("please choose from the following options")
            charChoice()
    charChoice()












    
        

