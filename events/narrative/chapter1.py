# importing for random number generation
import random
from miscellaneous.misc import errHandle

# function to determine likelihood of random combat encounter
def ambush():
    amAmbushed = random.randrange(1,21)



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
    elif choice == "B" or choice == "b":
        print("enter west wing")
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
    elif choice == "B" or choice == "b":
        print("enter east wing")
    elif choice == "C" or choice == "c":
        print("You return to landing.")
        landing()
    else:
       errHandle(headingWest)

    





