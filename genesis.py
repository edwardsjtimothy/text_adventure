#importing creature constructor function
from creatures.adventurers import Wizard, Rogue, Barbarian
from creatures.monsters import Skeleton




ancientSkeleton = Skeleton("Ancient Skeleton", 5, 10)

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
        print("""
            You have selected Wizard!
            Here are you starting stats.
        """)
        global wizard
        wizard = Wizard(name, 10, 20)
        stats = """
            ||Name: {} ||
            ||Health: {} ||
            ||Mana: {} ||
        """
        print(stats.format(wizard.name, wizard.health, wizard.mana))
        

    elif choice == "B" or choice =="b":
        print("""
            You have selected Rogue!
            Here are you starting stats.
        """)
        char = Rogue(name, 15, 100)
        stats = """
            ||Name: {} ||
            ||Health: {} ||
            ||Focus: {} ||
        """
        print(stats.format(char.name, char.health, char.focus))
       
        
    elif choice == "C" or choice =="c":             
        print("""
            You have selected Rogue!
            Here are you starting stats.
        """)
        char = Barbarian(name, 20, 100)
        stats = """
            ||Name: {} ||
            ||Health: {} ||
            ||Max Rage: {} ||
        """
        print(stats.format(char.name, char.health, char.rage))

#combat encounter
def wizEncounter(player, target):
    print("An enemy approaches...")
    action = input("""
            A: Engage 
            B: Manuver
            C: Retreat
                """)
    if action == "A" or action == "a":
        print("How will you engage?")
        action = input("""
                A: Melee
                B: Fireball
                C: Augury
            """)
        if action == "A" or action == "a":
            wizard.melee(target)
        elif action == "B" or action == "b":
            wizard.fireball(target)
        elif action == "C" or action == "c":
            wizard.augury(target) 
            
    
        if target.health > 0:
            encounter(player, target)

main()
encounter(wizard, ancientSkeleton)


    
        

