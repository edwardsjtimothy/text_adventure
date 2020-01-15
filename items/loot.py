#random number module
import random

wizLoot = {
        common: {
            consNames: {
                first: ["Minor Potion of ", "Minor Salve of ", "Minor Tincture of ", "Minor Draught of "],
                second: ["Common ", "Base ", "Unremarkable ", "Limited ", "Lilliputian " ],
            },
            wepNames: ["Shepard's ", "Watchman's ", "Initiate's ", "Novice's ", "Training ", "Rough ", "Unfinished ", "Shoddy ", "Bent ", "Broken ", "Unremarkable ", "Hermit's "],
            armNames: ["Shepard's ", "Initiate's ", "Novice's ", "Training ", "Rough ", "Unfinished ", "Shoddy ", "Bent ", "Broken ", "Unremarkable ", "Plain", "Roughspun", "Threadbare", "Linen", "Woollen", "Moth-eaten ", "Moldy ", "Mildewed ", "Sweaty ", "Hermit's "],
        },
        rare: {
            consumable: {
                first: ["Potion of ", "Salve of ", "Tincture of ", "Draught of "],
                second: ["Remarkable ", "Exceptional ", "Stupendous ", "Great ", "Encompassing ", "Significant ", "Miraculous "],
            }, 
            first: ["Artificer's ", "Magister's ", "Nobleman's ", "Lord's ", "Vizier's ", "Senechal's", "Wiseman's", "Castellan's ", "Alchemist's ", "Courtier's ", "Magician's ", "Conjurer's"],
            second: ["of Unbridled Power", "of Tremendous Force", "of Transcendant Gnosis", "of Adamantine Will", "of Mystical Knowledge", "of Terrible Knowledge", "of Creeping Madness", "of Silent Tragedy", "of Inexorable Decay", "of Inexhaustible Wisdom", "of Deepest Regret", "of Crackling Lightning", "of the Rolling Tide", "of the Drowned", "of the Wise","of Deepest Night", "of Glorious Folly", "of Inscessant Need", "of Gathering Storms", "of Yawning Darkness", "of Brightest Day", "of Corrupted Vision", "of Occulted Vision", "of Unending Laughter", "of Riotous Banishment","of Everlasting Wisdom", "of Endless Magic", "of Silent Deceit", "of Boundless Joy", "of Corrosive Belief", "of Radiant Power", "of Powerful Radiance", "of Benthic Life", "of Chthonic Reserve", "of Waking Dreams", "of Deepest Regret", "of Gaurdian Spirits", "of Unholy Need", "of Phantasmagorical Beasts", "of Terrible Certainty", "of Undying Longing", "of Astral Protection", "of Thunderous Force", "of Fulminating Power", "of Corsecating Light", "of Far off Lands", "of Spun Moonlight", "of Spun Shadow", "of Rending Fear", "of Teeming Life", "of Woven Nightmare", "of Civilization's End", "of Superluminal Motion", "of Limitless Power", "of Infinite Tears", "of Primordial Matter", "of the Warp and Weft", "of the Spaces Between", "of Transposital Realities", "of the True Path", "of Stygian Wind"],
        },
        wondrous: {
            consumable: {
                first: ["Greater Potion of ", "Greater Salve of ", "Greater Tincture of ", "Greater Draught of "],
                second: ["Demigod's ", "Protean ", "Primordial ", "Unmatched ", "Unbound ", "Colosal"],
            },
            first: ["Gabrathian's ", "Everad's ", "Almighty ", "Mastercrafted ", "Ancient Relic-","Primordial ","Unparalleled ","Potent Heirloom ", "Divine ", "Worldbreaker ", "Mobius ", "Cosmic ", "Imprisoned ", "Zaartrax's "],
            second: [", the Unending", ", Breaker of Minds", ", the Dark Bane", ", the Death of Fools", ", Mage's Folly", ", the Finger of God", ", Avatar of Creation", ", the Great Change", ", the Sleeper", ", the Toller of the Bell", ", the Rushing Fate", ", Darkness", ", Light", ", the One Who Eats", ", Infinity's Grasp", ", Falling Through Time", ", Destruction", ", It That Thirsts", ", the End", ", Heat Death", ", Pantheon's Fall", ", Creation Unbound", ", the Bounty of Chaos", ", Mortal's Folly", ", Magebane", ", the Unknowable", ", Time's Woesome Tide", ", the Walker", ", the Waker", ", the Sleeper", ", the Key", ", Prometheus Bound", ", Gravity's Edge" ],
        },
        potType: ["Healing", "Magical Force", "Mana Regeneration"],
        wepType: ["Staff ", "Dagger ", "Blade ", "Anthame ", "Wand ", "Shillelagh ", "Poniard ", "Shiv ", "Rod ", "Club ", "Willow Switch ", "Branch "],
        armType: ["Robe ", "Vest ", "Gloves ", "Pants ", "Boots ", "Slippers ", "Crown ", "Headdress ", "Belt ", "Cord ", "Headband ", "Shirt ", "Kimono ", "Sandals ", "Gown", "Toga",],
    },

    # rogue loot table
    # barbarian loot table
