# importing for random number generation
import random
from misc import errHandle

def exposition():
    print("""

    ...You move to stand at the edge of the opening, the anchored piton a few paces behind you. You speak one final syllable that jangles, painful and bitter in your mouth. Tasting iron, you feel your harness strain slightly as a sibilant tension fills the air and rattles something in your head, just beyond the range of your hearing. You look down into the yawning maw before you. Once again a breeze, so cool as to be cold, rises to play over your skin. You spare a final glance for the grassy glade and the deepening twilight. You tip forward and fall into darkness.
    
                                                                            **********CHAPTER 1: DESCENT**********

     """)

# entering dungeon
def descent():
    print(""" 
    ****************************************************************************************************************************************************************************************
    Descending into darkness
    ****************************************************************************************************************************************************************************************
    """)

    choice = input(""" 
        A: Look at the roof.
        B: Reach the bottom.
    """)
    if choice == "A" or choice == "a":
        print(" Describe frescos on dome")
        descent()
    elif choice == "B" or choice == "b":
        print("landing")
        landing()
    else:
        errHandle(descent)

#central chamber

def landing():
    print(""" 
    *****************************************************************************************************************************************************************************************
    Sandy bottom near dropped torch. Scuffles in the sand lead away to the west. Can see markings on floor where sand is disturbed. Sand is smooth and flat to the east. 
    *****************************************************************************************************************************************************************************************
    """)
    choice = input(""" 
        A: Investigate floor.
        B: Head west.
        C: Head east. 
        """)
    if choice == "A" or choice == "a":
        print("Describe carvings on floor.")
        landing()
    elif choice == "B" or choice == "b":
        print("head west")
        headingWest()
    elif choice == "C" or choice == "c":
        print("head east")
        headingEast()
    else:
       errHandle(landing)

def headingWest():
    print("""
    *****************************************************************************************************************************************************************************************
    Describe path west and scene at entry to West Wing. Remains of a ill-fated expeditionary party. Describe cavernous entry to west wing.  
    *****************************************************************************************************************************************************************************************
    """)
    choice = input(""" 
        A: Investigate remains.
        B: Enter West Wing.
        C: Return to landing.
                    """)
    if choice == "A" or choice == "a":
        print("Describe remains")
        headingWest()
    elif choice == "B" or choice == "b":
        westWingEntrance()
    elif choice == "C" or choice == "c":
        print("You return to landing.")
        landing()
    else:
       errHandle(headingWest)

def headingEast():
    print(""" 
    *****************************************************************************************************************************************************************************************
    Describe path east and scene closer to entry. Signs of a ancient battle. Pitted floor and walls. Cavernous entrance to East wing scarred.
    *****************************************************************************************************************************************************************************************
    """)
    choice = input(""" 
        A: Investigate battlefield.
        B: Enter East Wing.
        C: Return to landing.
                    """)
    if choice == "A" or choice == "a":
        print("Describe battlefield")
        headingEast()
    elif choice == "B" or choice == "b":
        eastWingEntrance()
    elif choice == "C" or choice == "c":
        print("You return to landing.")
        landing()
    else:
       errHandle(headingEast)

# westwing 

def westWingEntrance():
    print(""" 
    ******************************************************************************************************************************************************************************************
    Entering west wing. Describe colonnaded passage, hundreds of feet high. Intricately carved. Sandy floor. Can move into the colonnade on the left and travel along the wall. Can do the same on the right. Can move down the middle. 
    ******************************************************************************************************************************************************************************************
    """)
    choice = input("""
        A: Move along right wall.
        B: Move along left wall.
        C: Move down middle.
        D: Return to central chamber.
    """)
    if choice == "A" or choice == "a":
        print("Describe path along left.")
    elif choice == "B" or choice == "b":
        print("Describe path along right")
    elif choice == "C" or choice == "c":
        print("Describe path down middle.")
    elif choice == "D" or choice == "d":
        print("Return to central chamber.")
        headingWest()
    else:
       errHandle(westWingEntrance)

# eastwing 

def eastWingEntrance():
    print(""" 
    ******************************************************************************************************************************************************************************************
    Entering east wing. Describe colonnaded passage, hundreds of feet high. Intricately carved. Sandy floor. Can move into the colonnade on the left and travel along the wall. Can do the same on the right. Can move down the middle. 
    ******************************************************************************************************************************************************************************************
    """)
    choice = input("""
        A: Move along right wall.
        B: Move along left wall.
        C: Move down middle.
        D: Return to central chamber.
    """)
    if choice == "A" or choice == "a":
        print("Describe path along left.")
    elif choice == "B" or choice == "b":
        print("Describe path along right")
    elif choice == "C" or choice == "c":
        print("Describe path down middle.")
    elif choice == "D" or choice == "d":
        print("Return to central chamber.")
        headingEast()
    else:
       errHandle(eastWingEntrance)







