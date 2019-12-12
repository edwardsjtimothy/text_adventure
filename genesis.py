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
        print(f"""
            ||Name: {wizard.name} ||
            ||Health: {wizard.health} ||
            ||Mana: {wizard.mana} ||
        """)

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
                A: Melee (no cost)
                B: Fireball (5 mana)
                C: Augury (15 mana)
            """)
        if action == "A" or action == "a":
            wizard.melee(target)
            target.abilitySelect(wizard)
        elif action == "B" or action == "b":
            wizard.fireball(target)
            target.abilitySelect(wizard)
        elif action == "C" or action == "c":
            wizard.augury(target) 
            target.abilitySelect(wizard)
    elif action == "B" or action == "b":
        print("manuver action")
    elif action == "C" or action == "c":
        print("retreat action")

    if target.health > 0:
        wizEncounter("Your foe still lives", target)
    elif target.health <= 0:
        print("Your enemy is slain!")
        print(f"""
            ||Name: {wizard.name} ||
            ||Health: {wizard.health} ||
            ||Mana: {wizard.mana} ||
        """)

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
                A: Melee (no cost)
                B: Punching Stab (20 focus)
                C: Shadow Strike (60 focus)
            """)
        if action == "A" or action == "a":
            rogue.melee(target)
            target.abilitySelect(rogue)
        elif action == "B" or action == "b":
            rogue.punchingStab(target)
            target.abilitySelect(rogue)
        elif action == "C" or action == "c":
            rogue.shadowStrike(target) 
            target.abilitySelect(rogue)
    elif action == "B" or action == "b":
        print("manuver action")
    elif action == "C" or action == "c":
        print("retreat action")

    if target.health > 0:
        rogEncounter("Your foe still lives", target)
    elif target.health <= 0:
        print("Your enemy is slain!")
        print(f"""
            ||Name: {rogue.name} ||
            ||Health: {rogue.health} ||
            ||Focus: {rogue.focus} ||
        """)

def barEncounter(flavor, target):
    print(flavor)
    action = input("""
            A: Engage 
            B: Manuver
            C: Retreat
                """)
    if action == "A" or action == "a":
        print("How will you engage?")
        action = input("""
                A: Melee (Generates rage)
                B: Savage Blow (Spends banked rage for extra dmg at a 3rg/1dmg ratio)
                C: Mortal Strike (50 rage: slays targets below 33% hp/dmg's those above 33%)
            """)
        if action == "A" or action == "a":
            barbarian.melee(target)
            target.abilitySelect(barbarian)
        elif action == "B" or action == "b":
            barbarian.savageBlow(target)
            target.abilitySelect(barbarian)
        elif action == "C" or action == "c":
            barbarian.mortalStrike(target) 
            target.abilitySelect(barbarian)
    elif action == "B" or action == "b":
        print("manuver action")
    elif action == "C" or action == "c":
        print("retreat action")

    if target.health > 0:
        barEncounter("Your foe still lives", target)
    elif target.health <= 0:
        print("Your enemy is slain!")
        print(f"""
            ||Name: {barbarian.name} ||
            ||Health: {barbarian.health} ||
            ||Rage: {barbarian.rage} ||
        """)










    
        

