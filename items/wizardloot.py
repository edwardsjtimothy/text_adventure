#random number module
import random 

class Wizardloot:
    consumableNames = {
        first: ["Draft of", "Potion of", "Salve of", "Tincture of"],
        second: ["Stupendous", "Mystical", "Miraculous", "Occult", "Esoteric", "Lightning", "Divine"],
        third: ["Healing", "Strength", "Fortitude", "Magical Force"]
    }

    weaponNames = {
        first: ["The", "Garblov's", "Paracelsus'"],
        second: ["Staff", "Dagger", "Blade", "Anthame", "Wand", "Shillelagh"],
        third: ["of Unbridled Power", "of Insidious Force", ", Wizard's Bane", "Death", "of Terrible Laughter", "Creeping Darkness", "Divine Radiance", "Thunderous Retort", "of the Unknown Frontier", "of Adamantine Will"]
    }
    consumable: False
    weapon: False
    armor: False

    def __init__(self, con, wep, arm):
        self.consumable = con
        self.weapon = wep
        self.armor = arm

        if self.
