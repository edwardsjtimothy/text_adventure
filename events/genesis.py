#importing creature constructor function
import random
from creatures.adventurers import Wizard, Rogue, Barbarian
from misc import errHandle

# exposition 
def exposition():
    print("""

    ...You move to stand at the edge of the opening, the anchored piton a few paces behind you. You speak one final syllable that jangles, painful and bitter in your mouth. Tasting iron, you feel your harness strain slightly as a sibilant tension fills the air and rattles something in your head, just beyond the range of your hearing. You look down into the yawning maw before you. Once again a breeze, so cool as to be cold, rises to play over your skin. You spare a final glance for the grassy glade and the deepening twilight. You tip forward and fall into darkness.
    
                                                                            **********CHAPTER 1: DESCENT**********

     """)

#main menu function
def main():
    exposition()
    print("                                                                       ************What is your name, traveller?************")
    global name
    name = input()
    if len(name) <= 0:
        print("Please enter a name...")
        main()
    else:
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
                ||Name: {wizard.name} ||
                ||Health: {wizard.health} ||
                ||Mana: {wizard.mana} ||
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
                ||Name: {rogue.name} ||
                ||Health: {rogue.health} ||
                ||Focus: {rogue.focus} ||
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
                ||Name: {barbarian.name} ||
                ||Health: {barbarian.health} ||
                ||Max Rage: {barbarian.rage} ||
            """)
        else:
            errHandle(charChoice)
    charChoice()
















    
        

