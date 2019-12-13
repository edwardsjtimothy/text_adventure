import random

#wizard combat encounter
def wizEncounter(flavor, target):
    from events.genesis import wizard
    print(flavor)
    # action menu
    action = input("""
            A: Engage 
            B: Maneuver
            C: Retreat
            D: Check Stats
                """)
    if action == "A" or action == "a":
        print("How will you engage?")
        action = input("""
                A: Melee (no cost)
                B: Fireball (10 mana)
                C: Augury (15 mana)
            """)
        # maneuver counter reset, player melee, enemy attack, check for player death
        if action == "A" or action == "a":
            target.maneuverCount = 0
            wizard.melee(target)
            target.abilitySelect(wizard)
            wizard.deathCheck()
        # maneuver counter reset, player fireball, enemy attack, check for player death
        elif action == "B" or action == "b":
            target.maneuverCount = 0
            wizard.fireball(target)
            target.abilitySelect(wizard)
            wizard.deathCheck()
        # maneuver counter reset, player augury, enemy attack, check for player death
        elif action == "C" or action == "c":
            target.maneuverCount = 0
            wizard.augury(target) 
            target.abilitySelect(wizard)
            wizard.deathCheck()
    # maneuver action, enemy attack, maneuver counter increment, check for player death
    elif action == "B" or action == "b":
        wizard.maneuver()
        target.abilitySelect(wizard)
        target.maneuverCount += 1
        wizard.deathCheck()
    elif action == "C" or action == "c":
        retreat = random.randrange(1, 11)
        if retreat > 4:
            print("running away successfully")
        elif 5 > retreat > 1:
            target.abilitySelect(wizard)
            wizard.deathCheck()
        elif retreat == 1:
            wizard.health = 0
            wizard.deathCheck()
    # displays current player stats
    elif action == "D" or action == "d":
        wizard.pulseCheck()

    # check if target is dead. If not, encounter runs again. 
    if target.health > 0:
        wizEncounter("Your foe still lives.", target)
    elif target.health <= 0:
        print("Your enemy is slain!")
        wizard.pulseCheck()

#rogue combat encounter 
def rogEncounter(flavor, target):
    from events.genesis import rogue
    print(flavor)
    # action menu
    action = input("""
            A: Engage 
            B: Maneuver
            C: Retreat
            D: Check Stats
                """)
    if action == "A" or action == "a":
        print("How will you engage?")
        action = input("""
                A: Melee (no cost)
                B: Punching Stab (20 focus)
                C: Shadow Strike (60 focus)
            """)
        # maneuver counter reset, player melee, enemy attack, check for player death
        if action == "A" or action == "a":
            target.maneuverCount = 0
            rogue.melee(target)
            target.abilitySelect(rogue)
            rogue.deathCheck()
        # maneuver counter reset, player punching stab, enemy attack, check for player death
        elif action == "B" or action == "b":
            target.maneuverCount = 0
            rogue.punchingStab(target)
            target.abilitySelect(rogue)
            rogue.deathCheck()
        # maneuver counter reset, player shadow strike, check for player death
        elif action == "C" or action == "c":
            target.maneuverCount = 0
            rogue.shadowStrike(target) 
            # enemy does not get a chance to attack when rogue uses Shadow Strike
            rogue.deathCheck()
    # maneuver action, enemy attack, maneuver counter increment, check for player death
    elif action == "B" or action == "b":
        rogue.maneuver()
        target.abilitySelect(rogue)
        target.maneuverCount += 1
        rogue.deathCheck()
    elif action == "C" or action == "c":
        retreat = random.randrange(1, 11)
        if retreat > 4:
            print("running away successfully")
        elif 5 > retreat > 1:
            target.abilitySelect(rogue)
            rogue.deathCheck()
        elif retreat == 1:
            rogue.health = 0
            rogue.deathCheck()
    # displays player stats
    elif action == "D" or action == "d":
        rogue.pulseCheck()

    # check if target is dead. If not, encounter runs again.
    if target.health > 0:
        rogEncounter("Your foe still lives.", target)
    elif target.health <= 0:
        print("Your enemy is slain!")
        rogue.pulseCheck()

def barEncounter(flavor, target):
    from events.genesis import barbarian
    print(flavor)
    action = input("""
            A: Engage 
            B: Maneuver
            C: Retreat
            D: Check Stats
                """)
    if action == "A" or action == "a":
        print("How will you engage?")
        action = input("""
                A: Melee (Generates rage)
                B: Savage Blow (Spends banked rage for extra dmg at a 3rg/1dmg ratio)
                C: Mortal Strike (50 rage: slays targets below 33% hp/dmg's those above 33%)
            """)
        # maneuver counter reset, player melee, enemy attack, check for player death
        if action == "A" or action == "a":
            target.maneuverCount = 0
            barbarian.melee(target)
            target.abilitySelect(barbarian)
            barbarian.deathCheck()
        # maneuver counter reset, player savage blow, enemy attack, check for player death
        elif action == "B" or action == "b":
            target.maneuverCount = 0
            barbarian.savageBlow(target)
            target.abilitySelect(barbarian)
            barbarian.deathCheck()
        # maneuver counter reset, player mortal strike, enemy attack, check for player death
        elif action == "C" or action == "c":
            target.maneuverCount = 0
            barbarian.mortalStrike(target) 
            target.abilitySelect(barbarian)
            barbarian.deathCheck()
     # maneuver action, enemy attack, maneuver counter increment, check for player death
    elif action == "B" or action == "b":
        barbarian.maneuver()
        target.abilitySelect(barbarian)
        target.maneuverCount += 1
        barbarian.deathCheck()
    elif action == "C" or action == "c":
        retreat = random.randrange(1, 11)
        if retreat > 4:
            print("running away successfully")
        elif 5 > retreat > 1:
            target.abilitySelect(barbarian)
            barbarian.deathCheck()
        elif retreat == 1:
            barbarian.health = 0
            barbarian.deathCheck()
    # display player stats
    elif action == "D" or action == "d":
        barbarian.pulseCheck()

     # check if target is dead. If not, encounter runs again.
    if target.health > 0:
        barEncounter("Your foe still lives.", target)
    elif target.health <= 0:
        print("Your enemy is slain!")
        barbarian.pulseCheck()