# importing for random number generation
import random

# function to determine likelihood of random combat encounter
def ambush():
    amAmbushed = random.randrange(1,21)
    print(amAmbushed)

def exposition():
    print("""

    ...You move to stand at the edge of the opening, the anchored piton a few paces behind you. You speak one final syllable that jangles, painful and bitter in your mouth. Tasting iron, you feel your harness strain slightly as a sibilant tension fills the air and rattles something in your head, just beyond the range of your hearing. You look down into the yawning maw before you. Once again a breeze, so cool as to be cold, rises to play over your skin. You spare a final glance for the grassy glade and the deepening twilight. You tip forward and fall into darkness.
    
                                                                            **********CHAPTER 1: DESCENT**********

     """)

# entering dungeon
def descent():
    print(""" 
    
    Descending in to darkness
    
    """)
    choice = input(""" 
        A: Look at the roof.
        B: Reach the bottom.
    """)

    if choice == "A" or "a":
        print(" Describe frescos on dome")
        descent()
    elif choice == "B" or "b":
        landing()




def landing():
    print(""" 
    
    Sandy bottom near dropped torch. Scuffles in the sand lead away to the west. Can see markings on floor where sand is disturbed. Sand is smooth and flat to the east. 
    
    """)
    choice = input(""" 
        A: Investigate floor.
        B: Head west.
        C: Head east. 
        """)
    if choice == "A" or "a":
        print("Describe carvings on floor.")
    elif choice == "B" or "b":
        print("head west")
    elif choice == "C" or "c":
        print("head east")
    





