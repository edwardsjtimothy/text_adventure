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
        landing()
    else:
        errHandle(descent)

#central chamber

def landing():
    print(""" 
    *****************************************************************************************************************************************************************************************
    You land softly and deactivate your harness. The ground is covered in fine white sand; it is perfectly smooth other than where it was disturbed by your arrival. Crouching, you brush it aside and uncover a floor.  You pick up your fallen torch and hold it high. In the widened circle of light, you see scuffles in the sand to the west that disappear into the darkness. To the east, the sand is smooth. 
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
        heading_west()
    elif choice == "C" or choice == "c":
        print("head east")
        heading_east()
    else:
       errHandle(landing)

def heading_west():
    print("""
    *****************************************************************************************************************************************************************************************
    You follow the scuffles in the sand as they head into the west. From the tracks, you estimate that several people headed this way, but how long ago you can't tell. After several hours of walking, the tracks grow more erratic. Soon you come across the remains of 4 or 5 humanoids before a massive opening in the west wall of the chamber. 
    *****************************************************************************************************************************************************************************************
    """)
    choice = input(""" 
        A: Investigate remains.
        B: Enter West Wing.
        C: Return to landing.
                    """)
    if choice == "A" or choice == "a":
        print("You move amongst the remains, kneeling beside each corpse in an effort to divine what may have killed them. The remains are very old; little is left but desiccated scraps of skin draped loosely over dry bones. Scuffles in the sand are frenzied and wild near the bodies. The party's gear lays where it fell; several of the people seem to have time to remove their packs in preparation to defend themselves. The rest fell where they stood, still encumbered by their equipment. You notice that their are no tracks in the sand leading to or from the cluster of dead. Whatever assailed them left no trace. In the remains of one of the packs, you find a hide tube sealed with wax.")
        heading_west()
    elif choice == "B" or choice == "b":
        west_wing_entrance()
    elif choice == "C" or choice == "c":
        print("You return to landing.")
        landing()
    else:
       errHandle(heading_west)

def heading_east():
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
        heading_east()
    elif choice == "B" or choice == "b":
        east_wing_entrance()
    elif choice == "C" or choice == "c":
        print("You return to landing.")
        landing()
    else:
       errHandle(heading_east)

# westwing 

def west_wing_entrance():
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
        heading_west()
    else:
       errHandle(west_wing_entrance)

# eastwing 

def east_wing_entrance():
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
        heading_east()
    else:
       errHandle(east_wing_entrance)







