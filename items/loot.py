#random number module
import random


class Loot:
    wizLoot = {
        common: {
            consNames: {
                first: ["Minor Potion of ", "Minor Salve of ", "Minor Tincture of ", "Minor Draught of "],
                second: ["Common ", "Base ", "Unremarkable ", "Limited ", "Lilliputian " ],
            },
            wepNames: {
                first: ["Shepard's ", "Watchman's ", "Initiate's ", "Novice's ", "Training ", "Rough ", "Unfinished ", "Shoddy ", "Bent ", "Broken ", "Unremarkable ", "Hermit's "],
            },
            armNames: {
                first: ["Shepard's ", "Initiate's ", "Novice's ", "Training ", "Rough ", "Unfinished ", "Shoddy ", "Bent ", "Broken ", "Unremarkable ", "Plain", "Roughspun", "Threadbare", "Linen", "Woollen", "Moth-eaten ", "Moldy ", "Mildewed ", "Sweaty ", "Hermit's "],
            }

        },
        

        rare: {
                consumable: {
                    first: ["Potion of ", "Salve of ", "Tincture of ", "Draught of "],
                    second: ["Remarkable ", "Exceptional ", "Stupendous ", "Great ", "Encompassing ", "Significant ", "Miraculous "],
                },
                weapon: {
                    first: ["Artificer's ", "Magister's ", "Nobleman's ", "Lord's ", "Vizier's ", "Senechal's", "Wiseman's", "Castellan's ", "Alchemist's ", "Courtier's ", "Magician's ", "Conjurer's"],
                    second: ["of Unbridled Power", "of Tremendous Force", "of Transcendant Gnosis", "of Adamantine Will", "of Mystical Knowledge", "of Terrible Knowledge", "of Creeping Madness", "of Silent Tragedy", "of Inexorable Decay", "of Inexhaustible Wisdom", "of Deepest Regret", "of Crackling Lightning", "of the Rolling Tide", "of the Drowned", "of the Wise","of Deepest Night", "of Glorious Folly", "of Inscessant Need", "of Gathering Storms", "of Yawning Darkness", "of Brightest Day", "of Corrupted Vision"],
                },
                armor: {
                    first: ["Artificer's ", "Magister's ", "Nobleman's ", "Lord's ", "Vizier's ", "Senechal's", "Wiseman's", "Castellan's ", "Alchemist's ", "Courtier's ", "Magician's ", "Conjurer's"],
                    second: [],
                }

        },

        wondrous: {
            consumable: {
                first: [],
                second: [],
                third: [],
            },
            weapon: {
                first: [],
                second: [],
                third: [],
            },
            armor: {
                first: [],
                second: [],
                third: [],
            }

        },

        potType: ["Healing", "Magical Force", "Mana Regeneration"],
        wepType: ["Staff", "Dagger", "Blade", "Anthame", "Wand", "Shillelagh", "Poniard", "Shiv", "Rod", "Club"],
        armType: ["Robe", "Vest", "Gloves", "Pants", "Boots", "Slippers", "Crown", "Headdress", "Belt", "Cord", "Headband", "Shirt", "Kimono", "Sandals"],
    },

    rogLoot = {
        common: {
            consumable: {
                first: [],
                second: [],
                third: [],
            },
            weapon: {
                first: [],
                second: [],
                third: [],
            },
            armor: {
                first: [],
                second: [],
                third: [],
            }

        },

        rare: {
            consumable: {
                first: [],
                second: [],
                third: [],
            },
            weapon: {
                first: [],
                second: [],
                third: [],
            },
            armor: {
                first: [],
                second: [],
                third: [],
            }

        },

        wondrous: {
            consumable: {
                first: [],
                second: [],
                third: [],
            },
            weapon: {
                first: [],
                second: [],
                third: [],
            },
            armor: {
                first: [],
                second: [],
                third: [],
            }

        }
    },

    barLoot = {
        common: {
            consumable: {
                first: [],
                second: [],
                third: [],
            },
            weapon: {
                first: [],
                second: [],
                third: [],
            },
            armor: {
                first: [],
                second: [],
                third: [],
            }

        },

        rare: {
            consumable: {
                first: [],
                second: [],
                third: [],
            },
            weapon: {
                first: [],
                second: [],
                third: [],
            },
            armor: {
                first: [],
                second: [],
                third: [],
            }

        },

        wondrous: {
            consumable: {
                first: [],
                second: [],
                third: [],
            },
            weapon: {
                first: [],
                second: [],
                third: [],
            },
            armor: {
                first: [],
                second: [],
                third: [],
            }

        }
    },

    consumable: False
    weapon: False
    armor: False

    def __init__(self, con, wep, arm):
        self.consumable = con
        self.weapon = wep
        self.armor = arm

        if self.

            consumableNames: {
                first: ["Draft of", "Potion of", "Salve of", "Tincture of"],
                second: ["Stupendous", "Mystical", "Miraculous", "Occult", "Esoteric", "Lightning", "Divine"],
                third: ["Healing", "Strength", "Fortitude", "Magical Force"]
            },

            weaponNames: {
                first: ["The", "Garblov's", "Paracelsus'"],
                second: ["Staff", "Dagger", "Blade", "Anthame", "Wand", "Shillelagh"],
                third: ["of Unbridled Power", "of Insidious Force", ", Wizard's Bane", "of Death", "of Terrible Laughter", "Creeping Darkness", "Divine Radiance", "Thunderous Retort", "of the Unknown Frontier", "of Adamantine Will"]
            },

            armorNames: {
                first: ["The", "Roughspun", "Common", "Uncanny", "Master-crafted", "Artisan", "Mythical", "Scholar's", "Explorer's", "Holy", "Accursed", "Clinging", "Snug", "Chaffing", "Tailored", "Nobleman's", "Aristocrat's", "Royal", "Emperor's", "Emperesses's", "Novice's", "Initiate's"],
                second: ["Robe", "Vest", "Gloves", "Pants", "Boots", "Slippers", "Crown", "Headdress", "Belt", "Cord" ],
                third: ["Restful Repose", "Winter Nights"]
            }
