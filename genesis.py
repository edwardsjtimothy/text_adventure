#importing creature constructor function
from creatures.adventurers import Wizard, Rogue, Barbarian

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
        global rogue
        rogue = Rogue(name, 15, 100)
        stats = """
            ||Name: {} ||
            ||Health: {} ||
            ||Focus: {} ||
        """
        print(stats.format(rogue.name, rogue.health, rogue.focus))
       
        
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

#wizard combat encounter
def wizEncounter(flavor, target):
    print(flavor)
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
    elif action == "B" or action == "b":
        print("manuver action")
    elif action == "C" or action == "c":
        print("retreat action")

    if target.health > 0:
        wizEncounter("Your foe still lives", target)
    elif target.health <= 0:
        print("Your enemy is slain!")

#rogue combat encounter 
def rogEncounter(flavor, target):
    print(flavor)
    action = input("""
            A: Engage 
            B: Manuver
            C: Retreat
                """)
    if action == "A" or action == "a":
        print("How will you engage?")
        action = input("""
                A: Melee
                B: Punching Stab
                C: Cloak of Shadows
            """)
        if action == "A" or action == "a":
            rogue.melee(target)
            target.abilitySelect(target.bludgeon(rogue), target.lumberingStrike(rogue), target.collapse())
        elif action == "B" or action == "b":
            rogue.punchingStab(target)
            target.abilitySelect(target.bludgeon(rogue), target.lumberingStrike(rogue), target.collapse())
        elif action == "C" or action == "c":
            rogue.cloakofShadows(target) 
            target.abilitySelect(target.bludgeon(rogue), target.lumberingStrike(rogue), target.collapse())
    elif action == "B" or action == "b":
        print("manuver action")
    elif action == "C" or action == "c":
        print("retreat action")

    if target.health > 0:
        rogEncounter("Your foe still lives", target)
    elif target.health <= 0:
        print("Your enemy is slain!") 
        

        
    
            




    
        

