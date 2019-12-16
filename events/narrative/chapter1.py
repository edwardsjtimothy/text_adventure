def exposition():
    print("""

    ...You move to stand at the edge of the opening, the anchored piton a few paces behind you. You speak one final syllable that jangles, painful and bitter in your mouth. Tasting iron, you feel your harness strain slightly as a sibilant tension fills the air and rattles something in your head, just beyond the range of your hearing. You look down into the yawning maw before you. Once again a breeze, so cool as to be cold, rises to play over your skin. You spare a final glance for the grassy glade and the deepening twilight. You tip forward and fall into darkness.
    
     """)

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
    elif choice == "B" or "b":
        print(" Describe landing.")



