# importing for random number generation
import random
from misc import errHandle

# entering dungeon
def descent():
    print(""" 
    ****************************************************************************************************************************************************************************************
    After plummetting through the gap, your descent at once slows to the rate of a falling feather as the harness takes your weight, its invisible tether anchored securely to the piton you hammered home above. The light of the dying sun recedes slowly away above you as the opening in the roof grows smaller with your decline. You can just make out something of the inside of the massive dome's ceiling in the rudy glow. You descend farther and farther into the vast darkness.
    ****************************************************************************************************************************************************************************************
    """)

    choice = input(""" 
        A: Look at the roof.
        B: Reach the bottom.
    """)
    if choice == "A" or choice == "a":
        print("The ceiling of the dome recedes slowly away from you as you drift down to the floor. What you can see of the ceiling is covered in vibrant mosaics, the subjects of which are too large to make out and stretch away into impenetrable darkness.")
        descent()
    elif choice == "B" or choice == "b":
        print("You reach the ground after a ")
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







