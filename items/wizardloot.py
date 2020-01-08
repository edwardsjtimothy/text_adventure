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
        third: ["of Unbridled Power", "of Insidious Force", ", Wizard's Bane", "of Death", "of Terrible Laughter", "Creeping Darkness", "Divine Radiance", "Thunderous Retort", "of the Unknown Frontier", "of Adamantine Will"]
    }

    armorNames = {
        first: ["The", "Roughspun", "Common", "Uncanny", "Master-crafted", "Artisan", "Mythical", "Scholar's", "Explorer's", "Holy", "Accursed", "Clinging", "Snug", "Chaffing", "Tailored", "Nobleman's", "Aristocrat's", "Royal", "Emperor's", "Emperesses's", "Novice's", "Initiate's"],
        second: ["Robe", "Vest", "Gloves", "Pants", "Boots", "Slippers", "Crown", "Headdress", "Belt", "Cord" ],
        third: ["Restful Repose", "Winter Nights"]
    }
    consumable: False
    weapon: False
    armor: False

    def __init__(self, con, wep, arm):
        self.consumable = con
        self.weapon = wep
        self.armor = arm

        if self.
