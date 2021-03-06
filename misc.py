import random
import enum

# error handling
def errHandle(fnc):
    print("                                                                     **********Please choose from the following options**********")
    fnc()


# loot generation function

def lootGen(rarity, ltType):
    firstWord = ""
    secondWord = ""
    thirdWord = ""
    itemName = ""
    conWepOrArm = random.randrange(1,4)

    if rarity == "common":
        # common consumable is generated
        if conWepOrArm == 1:
            firstWord = ltType[0]["common"]["consumable"]["first"][random.randrange(0 , len(ltType[0]["common"]["consumable"]["first"]))]
            secondWord = ltType[0]["common"]["consumable"]["second"][random.randrange(0 , len(ltType[0]["common"]["consumable"]["second"]))]
            thirdWord = ltType[0]["potType"][random.randrange(0 , len(ltType[0]["potType"]))]
            itemName = firstWord + secondWord + thirdWord
            return itemName
        elif conWepOrArm == 2:
        # common armor is generated
            firstWord = ltType[0]["common"]["armNames"][random.randrange(0 , len(ltType[0]["common"]["armNames"]))]
            secondWord = ltType[0]["armType"][random.randrange(0 , len(ltType[0]["armType"]))]
            itemName = firstWord + secondWord
            return itemName
        elif conWepOrArm == 3:
        # common weapon is generated
            firstWord = ltType[0]["common"]["wepNames"][random.randrange(0 , len(ltType[0]["common"]["wepNames"]))]
            secondWord = ltType[0]["wepType"][random.randrange(0 , len(ltType[0]["wepType"]))]
            itemName = firstWord + secondWord
            return itemName
    elif rarity == "rare":
        # rare consumable is generated
        if conWepOrArm == 1:
            firstWord = ltType[0]["rare"]["consumable"]["first"][random.randrange(0 , len(ltType[0]["rare"]["consumable"]["first"]))]
            secondWord = ltType[0]["rare"]["consumable"]["second"][random.randrange(0 , len(ltType[0]["rare"]["consumable"]["second"]))]
            thirdWord = ltType[0]["potType"][random.randrange(0 , len(ltType[0]["potType"]))]
            itemName = firstWord + secondWord + thirdWord
            return itemName
        # rare armor is generated
        elif conWepOrArm == 2:
            firstWord = ltType[0]["rare"]["armFirst"][random.randrange(0 , len(ltType[0]["rare"]["armFirst"]))]
            secondWord = ltType[0]["armType"][random.randrange(0 , len(ltType[0]["armType"]))]
            thirdWord = ltType[0]["rare"]["second"][random.randrange(0 , len(ltType[0]["rare"]["second"]))]
            itemName = firstWord + secondWord + thirdWord
            return itemName
        # rare weapon is generated
        elif conWepOrArm == 3:
            firstWord = ltType[0]["rare"]["wepFirst"][random.randrange(0 , len(ltType[0]["rare"]["wepFirst"]))]
            secondWord = ltType[0]["wepType"][random.randrange(0 , len(ltType[0]["wepType"]))]
            thirdWord = ltType[0]["rare"]["second"][random.randrange(0 , len(ltType[0]["rare"]["second"]))]
            itemName = firstWord + secondWord + thirdWord
            return itemName
    elif rarity == "wondrous":
        # wondrous consumable is generated
        if conWepOrArm == 1:
            firstWord = ltType[0]["wondrous"]["consumable"]["first"][random.randrange(0 , len(ltType[0]["wondrous"]["consumable"]["first"]))]
            secondWord = ltType[0]["wondrous"]["consumable"]["second"][random.randrange(0 , len(ltType[0]["wondrous"]["consumable"]["second"]))]
            thirdWord = ltType[0]["potType"][random.randrange(0 , len(ltType[0]["potType"]))]
            itemName = firstWord + secondWord + thirdWord
            return itemName
        # wondrous armor is generated
        elif conWepOrArm == 2:
            firstWord = ltType[0]["wondrous"]["first"][random.randrange(0 , len(ltType[0]["wondrous"]["first"]))]
            secondWord = ltType[0]["armType"][random.randrange(0 , len(ltType[0]["armType"]))]
            thirdWord = ltType[0]["wondrous"]["armSecond"][random.randrange(0 , len(ltType[0]["wondrous"]["armSecond"]))]
            itemName = firstWord + secondWord + thirdWord
            return itemName
        # wondrous weapon is generated
        elif conWepOrArm == 3:
            firstWord = ltType[0]["wondrous"]["first"][random.randrange(0 , len(ltType[0]["wondrous"]["first"]))]
            secondWord = ltType[0]["wepType"][random.randrange(0 , len(ltType[0]["wepType"]))]
            thirdWord = ltType[0]["wondrous"]["wepSecond"][random.randrange(0 , len(ltType[0]["wondrous"]["wepSecond"]))]
            itemName = firstWord + secondWord + thirdWord
            return itemName

# Loot tables for each class 

wizLoot = {
    "common": {
        "consumable": {
            "first": ["Minor Potion of ", "Minor Salve of ", "Minor Tincture of ", "Minor Draught of "],
            "second": ["Common ", "Base ", "Unremarkable ", "Limited ", "Lilliputian " ],
        },
        "wepNames": ["Shepard's ", "Watchman's ", "Initiate's ", "Novice's ", "Training ", "Rough ", "Unfinished ", "Shoddy ", "Bent ", "Broken ", "Unremarkable ", "Hermit's "],
        "armNames": ["Shepard's ", "Initiate's ", "Novice's ", "Training ", "Rough ", "Unfinished ", "Shoddy ", "Unremarkable ", "Plain ", "Roughspun ", "Threadbare ", "Linen ", "Woollen ", "Moth-eaten ", "Moldy ", "Mildewed ", "Sweaty ", "Hermit's ", "Stained ", "Fraying "],
    },
    "rare": {
        "consumable": {
            "first": ["Potion of ", "Salve of ", "Tincture of ", "Draught of "],
            "second": ["Remarkable ", "Exceptional ", "Stupendous ", "Great ", "Encompassing ", "Significant ", "Miraculous "],
        }, 
        "wepFirst": ["Artificer's ", "Magister's ", "Nobleman's ", "Lord's ", "Vizier's ", "Senechal's ", "Wiseman's ", "Castellan's ", "Alchemist's ", "Courtier's ", "Magician's ", "Conjurer's ", ],
        "armFirst": ["Artificer's ", "Magister's ", "Nobleman's ", "Lord's ", "Vizier's ", "Senechal's ", "Wiseman's ", "Castellan's ", "Alchemist's ", "Courtier's ", "Magician's ", "Conjurer's "],
        "second": ["of Unbridled Power", "of Tremendous Force", "of Transcendant Gnosis", "of Adamantine Will", "of Mystical Knowledge", "of Terrible Knowledge", "of Creeping Madness", "of Silent Tragedy", "of Inexorable Decay", "of Inexhaustible Wisdom", "of Deepest Regret", "of Crackling Lightning", "of the Rolling Tide", "of the Drowned", "of the Wise","of Deepest Night", "of Glorious Folly", "of Inscessant Need", "of Gathering Storms", "of Yawning Darkness", "of Brightest Day", "of Corrupted Vision", "of Occulted Vision", "of Unending Laughter", "of Riotous Banishment","of Everlasting Wisdom", "of Endless Magic", "of Silent Deceit", "of Boundless Joy", "of Corrosive Belief", "of Radiant Power", "of Powerful Radiance", "of Benthic Life", "of Chthonic Reserve", "of Waking Dreams", "of Deepest Regret", "of Gaurdian Spirits", "of Unholy Need", "of Phantasmagorical Beasts", "of Terrible Certainty", "of Undying Longing", "of Astral Protection", "of Thunderous Force", "of Fulminating Power", "of Corsecating Light", "of Far off Lands", "of Spun Moonlight", "of Spun Shadow", "of Rending Fear", "of Teeming Life", "of Woven Nightmare", "of Civilization's End", "of Superluminal Motion", "of Limitless Power", "of Infinite Tears", "of Primordial Matter", "of the Warp and Weft", "of the Spaces Between", "of Transposital Realities", "of the True Path", "of Stygian Wind"],
    },
    "wondrous": {
        "consumable": {
            "first": ["Greater Potion of ", "Greater Salve of ", "Greater Tincture of ", "Greater Draught of "],
            "second": ["Demigod's ", "Protean ", "Primordial ", "Unmatched ", "Unbound ", "Colosal"],
        },
        "first": ["Gabrathian's ", "Everad's ", "Almighty ", "Mastercrafted ", "Ancient Relic-","Primordial ","Unparalleled ","Potent Heirloom ", "Divine ", "Worldbreaker ", "Mobius ", "Cosmic ", "Imprisoned ", "Zaartrax's "],
        "wepSecond": [", the Unending", ", Breaker of Minds", ", the Dark Bane", ", the Death of Fools", ", Mage's Folly", ", the Finger of God", ", Avatar of Creation", ", the Great Change", ", the Sleeper", ", the Toller of the Bell", ", the Rushing Fate", ", Darkness", ", Light", ", the One Who Eats", ", Infinity's Grasp", ", Falling Through Time", ", Destruction", ", It That Thirsts", ", the End", ", Heat Death", ", Pantheon's Fall", ", Creation Unbound", ", the Bounty of Chaos", ", Mortal's Folly", ", Magebane", ", the Unknowable", ", Time's Woesome Tide", ", the Waker", ", the Key", ", Prometheus Bound", ", Gravity's Edge", ", the Lock", ", It That Binds", ", the Lock"],
        "armSecond": [", Infinity's Garb", ", Silence Enthroned", ", the Garb of the Wayward Mage", ", the Beckoning", ", Sanctuary's Kiss", ", the Ancient Madness", ", Vision Unrestrained", ", Twist of Time", ", Causality Unwound", ", Garb of Canopic Preservation", ", the Fractal Twist", ", the Endless Warmth",]
    },
    "potType": ["Healing", "Magical Force", "Mana Regeneration"],
    "wepType": ["Staff ", "Dagger ", "Blade ", "Anthame ", "Wand ", "Shillelagh ", "Poniard ", "Shiv ", "Rod ", "Club ", "Willow Switch ", "Branch "],
    "armType": ["Robe ", "Vest ", "Gloves ", "Pants ", "Boots ", "Slippers ", "Crown ", "Headdress ", "Belt ", "Cord ", "Headband ", "Shirt ", "Kimono ", "Sandals ", "Gown ", "Toga ", "Amice ", "Shawl ", "Wrappings ", "Cloak ", "Cape "],
    },

rogLoot = {
    "common": {
        "consumable": {
            "first": ["Minor Potion of ", "Minor Salve of ", "Minor Tincture of ", "Minor Draught of "],
            "second": ["Common ", "Base ", "Unremarkable ", "Limited ", "Lilliputian " ],
        },
        "wepNames": ["Cutpurse's ", "Watchman's ", "Initiate's ", "Novice's ", "Training ", "Rough ", "Unfinished ", "Shoddy ", "Bent ", "Broken ", "Unremarkable ", "Highwayman's ","Street Urchin's ", "Militia's ", "Bandit's "],
        "armNames": ["Cutpurse's ", "Bandit's ", "Initiate's ", "Novice's ", "Training ", "Rough ", "Unfinished ", "Shoddy ", "Stained ", "Fraying " "Unremarkable ", "Plain ", "Grimy ", "Threadbare ", "Bloodstained ", "Studded ", "Punctured ", "Worn ", "Slimy ", "Rotten ", "Watchman's ", "Moldy ", "Mildewed ", "Sweaty ", "Street Urchin's ", "Militia's ", "Streetfighter's"],
    },
    "rare": {
        "consumable": {
            "first": ["Potion of ", "Salve of ", "Tincture of ", "Draught of "],
            "second": ["Remarkable ", "Exceptional ", "Stupendous ", "Great ", "Encompassing ", "Significant ", "Miraculous "],
        }, 
        "wepFirst": ["Nobleman's ", "Lord's ", "Castellan's ", "Courtier's ", "Syndicate's ", "Blacksteel ", "Shadowy ", "Silent ", "Striking ", "Tearing ", "Ripping ", "Piercing ", "Punching ", "Weighted ", "Featherlight ", "Spring-loaded ", "Concealable ", "Hidden ", "Marshall's ", "Lawman's ", "Dungeoneer's ", "Explorer's ", "Finely Crafted ", "Well Wrought ", "Heavy ", "Crushing ", "Hissing ", "Dexterous "],
        "armFirst": ["Nobleman's ", "Lord's ", "Castellan's ", "Courtier's ", "Syndicate's ", "Blacksteel ", "Shadowy ", "Silent ", "Striking ", "Featherlight ", "Marshall's ", "Lawman's ", "Dungeoneer's ", "Explorer's ", "Finely Crafted ", "Well Wrought ", "Dexterous ", "Supple ", "Flexible ", "Reliable ", "Concealing ", "Moondark "],
        "second": ["of Unseen Attacks", "of Tremendous Cunning", "of Adamantine Will", "of Silent Tragedy", "of Deepest Regret", "of Traveler's Bane", "of Deepest Night", "of Glorious Folly", "of Inscessant Need", "of Moonless Nights", "of Silent Deceit", "of Far off Lands", "of Clouded Moonlight", "of Flickering Shadows", "of Resolute Calm", "of Widow's Tears", "of the Darkstalker", "of Grasping Oppertunity", "of Riches Unclaimed", "of Allies Betrayed", "of Unseen Attacks", "of Bloodied Cobblestones", "of Silenced Screams", "of Missing Sentries", "of Plundered Reliquaries", "of Toppled Kings", "of Slit Purse Strings", "of Perfect Moment", "of Acrobat's Grace", "of Well-timed Blows", "of Jarring Ripostes", "of Offhanded Attacks", "of Inevitable Riches", "of Exposed Vitals", "of Hidden Ingress", "of Well-laid Schemes", "of Plundered Tombs", "of Queensbane", "of Profitable Venture's", "of Cunning Strategy", "of Whip-crack Speed", "of Stunning Blows"],
    },
    "wondrous": {
        "consumable": {
            "first": ["Greater Potion of ", "Greater Salve of ", "Greater Tincture of ", "Greater Draught of "],
            "second": ["Masterthief's ", "Career Assassin's ", "Lifelong ", "Unmatched ", "Unbound ", "Colosal"],
        },
        "first": ["Tishna's ", "Ar'marad's ", "Treasurehoard ", "Mastercrafted ", "Ancient Relic-","Primordial ","Unparalleled ","Potent Heirloom ", "Inherited ", "Primordial ", "Transpositional ", "Cosmic ", "Precognitive ", "Arine's "],
        "wepSecond": [", the Dark Bane", ", the Death of Fools", ", Tombraider's Folly", ", the Finger of God", ", Avatar of Stealth", ", the Ferryman", ", the Sleeper", ", the Toller of the Bell", ", the Rushing Fate", ", Darkness", ", Rushing Death", ", the One Who Eats", ", Infinity's Strike", ", Anticipation Unbridled", ", Destruction", ", It That Thirsts", ", the End", ", Death", ", Pantheon's Fall", ", Lineages Unmade", ", Avarice Unbound", ", the Bounty of Ambition", ", Mortal's Folly", ", Theifsbane", ", the Undone", ", Woe Betide", ", the Walker", ", the Waker", ", the Key", ", Prometheus Bound", ", Gravity's Edge", ", the Lock", ", It That Bleeds", ", the Lock"],
        "armSecond": [", the Unheard's Garb", ", Silence Enthroned", ", the Garb of the Wayward Cutpurse", ", the Beckoning", ", Stealth's Kiss", ", the Ancient Ways", ", Vision Unrestrained", ", Twist of Fate", ", Causality Unwound", ", Garb of Deflecting Darkness", ", the Fractal Twist", ", Oppertunity Unending",]
    },
    "potType": ["Healing", "Critical Damage", "Focus Regeneration"],
    "wepType": ["Mace ", "Dagger ", "Blade ", "Shortsword ", "Stiletto ", "Bootknife ", "Poniard ", "Shiv ", "Brushknife ", "Club ", "Rapier ", "Knuckledusters ","Thowing Dagger ", "Hatchet ", "Wristblade ", "Fingerknife ", "Scimitar ", "Cutlace ", "Cestus ", "Kukri "],
    "armType": ["Jerkin ", "Vest ", "Gloves ", "Pants ", "Boots ", "Facemask ", "Belt ", "Cord ", "Headband ", "Shirt ", "Scalemail ", "Sandals ", "Shoulderguards ", "Headwrap ", "Bandolier ", "Cloak ", "Cape", "Bracers ", "Greaves " ],
    },

barLoot = {
    "common": {
        "consumable": {
            "first": ["Minor Potion of ", "Minor Salve of ", "Minor Tincture of ", "Minor Draught of "],
            "second": ["Common ", "Base ", "Unremarkable ", "Limited ", "Lilliputian " ],
        },
        "wepNames": ["Combatant's ", "Brawler's ", "Soldier's ", "Primitive ", "Initiate's ", "Novice's ", "Training ", "Rough ", "Unfinished ", "Shoddy ", "Bent ", "Broken ", "Unremarkable ", "Warrior's ","Thug's ", "Militia's ", "Grunt's "],
        "armNames": ["Combatant's ", "Brawler's ", "Soldier's ", "Primitive ", "Initiate's ", "Novice's ", "Training ", "Rough ", "Unfinished ", "Shoddy ", "Stained ", "Fraying " "Unremarkable ", "Plain ", "Grimy ", "Threadbare ", "Bloodstained ", "Studded ", "Punctured ", "Worn ", "Slimy ", "Rotten ", "Moldy ", "Mildewed ", "Sweaty ", "Thug's ", "Militia's ", "Streetfighter's"],
    },
    "rare": {
        "consumable": {
            "first": ["Potion of ", "Salve of ", "Tincture of ", "Draught of "],
            "second": ["Remarkable ", "Exceptional ", "Stupendous ", "Great ", "Encompassing ", "Significant ", "Miraculous "],
        }, 
        "wepFirst": ["Marshall's ", "Lord's ", "Castellan's ", "Dynastic ", "Lieutenant's ", "Castle-forged ", "Commander's ", "Crushing ", "Heavy ", "Massive ", "Bone-breaking ", "Weighted ", "Marshall's ", "Executioner's ", "Dungeoneer's ", "Explorer's ", "Finely Crafted ", "Well Wrought ", "Powerful ", "Tribal ", "Ancient "],
        "armFirst": ["Marshall's ", "Lord's ", "Castellan's ", "Dynastic ", "Lieutenant's ", "Castle-forged ", "Commander's ", "Heavy ", "Protective ", "Marshall's ", "Juggernaught's ", "Fighter's ", "Nomadic ", "Finely Crafted ", "Well Wrought ", "Reliable ", "Bloodied ",],
        "second": ["of Unbridled Strength", "of Tremendous Force", "of Adamantine Resolve", "of Bloody Tragedy", "of Deepest Rage", "of Traveler's Bane", "of Bloodlust", "of Glorious Folly", "of Inscessant Need", "of Sleepless Nights", "of Screaming Violence", "of Far off Lands", "of Clouded Thought", "of Pounding Rage", "of Ephemeral Calm", "of Widow's Tears", "of the Bloodstalker", "of Roiling Fury", "of Quaking Steps", "of Slain Foes", "of Brutal Attacks", "of Bloodied Limbs", "of Bellowing Challenge", "of Slaughtered Sentries", "of Will Deposed", "of Toppled Kings", "of Broken Foes", "of Perfect Strikes", "of Incandescent Fury", "of Well-timed Blows", "of Jarring Attacks", "of Unstoppable Charges", "of Inevitable Victory", "of Rushing Charge", "of Dismembered Enemies", "of Racing Glory", "of Plundered Ruins", "of Queensbane", "of Flowing Vitae", "of Brutal Cunning", "of Thunderous Speed", "of Stunning Blows"],
    },
    "wondrous": {
        "consumable": {
            "first": ["Greater Potion of ", "Greater Salve of ", "Greater Tincture of ", "Greater Draught of "],
            "second": ["Battlemaster's ", "Indomitable ", "Potent ", "Unmatched ", "Unbound ", "Colosal"],
        },
        "first": ["Barduk's ", "Torgan's ", "Peerless ", "Mastercrafted ", "Ancient Relic-","Primordial ","Unparalleled ","Potent Heirloom ", "Inherited ", "Primordial ", "Worldbreaker ", "Cosmic ",],
        "wepSecond": [", the Rending Bane", ", the Death of Fools", ", Tombraider's Folly", ", the Finger of God", ", Avatar of Destruction", ", the Ferryman", ", the Sleeper", ", the Toller of the Bell", ", the Rushing Fate", ", Darkness", ", Rushing Death", ", the One Who Eats", ", Infinity's Mallice", ", Violence Unbridled", ", Destruction", ", It That Thirsts", ", the End", ", Death", ", Pantheon's Fall", ", Lineages Unmade", ", Strife Unbound", ", the Bounty of Conquest", ", Mortal's Folly", ", Warriorsbane", ", the Undone", ", Woe Betide", ", the Walker", ", the Waker", ", the Key", ", Prometheus Slain", ", Gravity's Edge", ", the Lock", ", It That Bleeds", ", the Lock"],
        "armSecond": [", the Unrelenting", ", Violence Enthroned", ", Armor of the Peerless Warrior", ", the Beckoning", ", Murder's Kiss", ", the Ancient", ", Violence Unrestrained", ", Twist of Fate", ", Causality Unwound", ", Might of Titans", ", the Aegis of Time", ", Bloodlust Unending",]
    },
    "potType": ["Healing", "Crushing Strikes", "Rage Generation"],
    "wepType": ["Mace ", "Greatsword ", "Longsword ", "Shortsword ", "Warhammer ", "Greataxe ", "Bastard Sword ", "Hand and a Half Sword ", "Zweihänder","Uchigatana ", "Claymore ", "Changdao ", "Mattock ", "Dory "],
    "armType": ["Gambeson ", "Greaves ", "Gauntlets ", "Cuisses ", "Sabatons ", "Vambraces ", "Belt ", "Cord ", "Headband ", "Shirt ", "Scalemail ", "Boots ", "Shoulderguards ", "Headwrap ", "Bandolier ", "Cloak ", "Cape", "Bracers ", "Greaves ", "Armingcap ", "Helm ", "Helmet ", "Pauldron "],
    },




